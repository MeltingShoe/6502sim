from modules.log import logger
from modules.testModule import thimg
from modules.latch import latch
from modules import utils
from modules.interface import interface
from modules import everyInterface as cons
from modules import registers as r
from modules import busses as b
from modules.PCInterfaces import PCInterface
from modules.alu import ALU
from modules import everyInterface
import traceback


logger.setLoggingLevel(1)


# ============TODO===================
# make the look in run() and add a reset()

# I still really want to find a way to make it so a clock would work.
# The OG 6502 was able to execute a single instruction every clock cycle
# For this it used clever routing through the 4 internal data busses and a 2 stage clock
# So different components activate on high clock and others activate on low clock
# I'm not exactly sure how to do this
# Like it would be easy enough to just make a clock bool that flips every time we go through the loop and
# everything that used the clock checked that flag every time it would try to run
# I'm worried about how the pass mosfets will function though. If I get the order of events wrong it would be
# possible for something to read when the bus hasn't been updated
# since the busses are full on registers in my program instead of just wires like IRL we could have WEIRD problems.
# so we probably want to like reset the bus at the start of the clock. Funny enough this means we're basically
# implementing the charge and drain mosfets i was certain wouldn't be relevant.
# for the most part we'd be fine if we just did all writes first then did reads. The pass mosfets would probably work fine
# if we just made sure they activated at the end of the first half of the clock.
# but i'm wondering about how more complex routing would work. It seems that getting data from the ACC into adress low is kinda hard
# like there's no pass mosfet, it looks like you'd have to go through the DOR and DL(or put it in BI and load O into AI).
# I'm not sure how often I'd need to do that routing, but I'd love to try to do things the 6502 to be so fast and efficient
# it can do a lot of instructions in way less cycles than other CPUs. It's like 1 instruction or memory operation per cycle
# ADC 0page takes 3, so i think it has to be one to get the instruction, one to get the page, and one to get the data.
# then i guess it does the add instantly? maybe they don't count reading the instruction.
# anyways in order to handle weird cases like this it might be good to force things to run in the right order.
# so like everything goes into a loop and anything that tries to read will check a flag on the bus to see if it's been written
# at this point I really think we should just go all in and simulate the full physical way that the 6502 work.
# so we'd have to essentially make everything run at the same time.
# this could honestly make things easier, since instead of saving function names in the CSV or making a function to
# decode the microcode into something that can run, we can just push control signals to every block.
# then I guess we just make every block go through and check if it's time to run.
# this would be easy if every component was connected to a clock
# doesn't look like it though???? at least the clocks aren't shown on the diagram but I will assume the things
# that don't show it do so because it's understood their control signals are ANDed with the clock and showing inputs from
# both clocks would clutter things.
# OK so brand new plan:
# We simulate the 2 clocks inside the cpu. We set this up in a way that allows us to simulate the OG functions of stepping
# the CPU with sync as well as the ability to hook a real clock up to a pin on the arduino(kit might have included 555 but mayb
# not cuz it's arduino, if not the RTC has clocks(1hz is easy, higher might be harder), or we could output a clock signal
# to a pin with arduino code and connect that to the input.) We could even hook up a real button to step the clock!
# until we get a real clock we simulate the clock in python. So we just give a bool that flips on a fixed increment
# and we convert that to 2 bools, one is inverted and both are delayed slightly(i think). Then we make every block
# have a function that checks their control signals and the clock state. If a control signal is on and the clock is in the right
# state, it runs the correct method. Then we just literally have a loop that calls every single block in the cpu.
# I think it's sort of unavoidable to have some sort of ordering to when things are run unfortunately.
# like unless we literally use threading to run things ayncronously I think it just has to happen
# and we do things to make sure everything runs in order like i have to think about when it's allowed to read or write from bus
# (writing to the bus more than once or reading an empty bus are both bad ideas)
# do we want to be intentionally inefficient? probably not. It might be best to not run the loop many times every clock cycle
# So if we're using a very slow clock or manually stepping the clock we want to know once our CPU has finished all the instructions
# it currently can. Actually I'm not even sure if we would ever need to run everything more than once in a single half clock
# Like if we do all writes on clock high and all reads on clock low I think we're just good.
# but then we are getting a little further away from the best simulation and hard coding more stuff.
# but at least having a way to detect that we've completed the work is important, so we can better analyze and
# calculate the optimal clock speed
# even using threads might not be too bad since in the end it's really just another way to put everything in a loop
# FIXING THE PASS MOSFETS:
# we need to add a flag to DB, SB, and ADH that says whether they've been written to(except the outside data bus)
# then when the pass mosfets run they check that flag and correctly transfer the data
# that flag is cleared at the start of the next full clock.
#
# If we do at least implement a queue we could make it so when a module tries to read from a bus that hasn't been written
# it goes back in the queue, but I'm fairly certain this condition will never happen so we probably don't need a queue
# lets at least go through in every function and make a check for that whenever we read and have it throw a warning
# so we never miss it.
#
# A simple way to do things that is unfortunately basically what we're already doing but does carry many benefits
# of full simulation would be:
# since every function only works if the control signal is 1, we'll have every function that runs a block start by
# checking it's control signals. if a signal is set, it will then check the clock. If that is also set,
# it will run the function. since we don't do anything if the control signal isn't set, we could just make it
# so that once the block has run this cycle it sets the control signal to 0
def main():
    alUnit = ALU()
    thimg.doIt()
    register1 = latch()
    register1.setData(17)
    register2 = latch()
    register2.setData(31)
    bus = latch()
    bus.setData(0)
    a = register1.getData()
    logger.debug('output ='+utils.arrToHex(a))
    a = register2.getData()
    logger.debug('output ='+utils.arrToHex(a))
    bridge1 = interface(register1, bus, name='[R1-B]')
    bridge2 = interface(register2, bus, name='[R2-B]')
    bridge1.writeToBus()
    bridge2.readFromBus()
    a = register1.getData()
    logger.debug('output ='+utils.arrToHex(a))
    a = register2.getData()
    logger.debug('output =', utils.arrToHex(a))
    PC = everyInterface.PC
    for i in range(0, 30):
        PC.I_PC()
    logger.info('PC count test complete. beginning alu test...')
    r.aInReg.setData([0, 0, 0, 1, 0, 0, 0, 1])
    r.bInReg.setData([0, 1, 0, 0, 1, 1, 1, 1])
    alUnit.add()
    out = r.sumReg.getData()
    logger.info('ALU output: ', out)


def run():
    try:
        main()
    except Exception as e:
        logger.error(e, traceback.format_exc())
    logger.saveLog()


if __name__ == "__main__":
    run()
