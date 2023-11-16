from modules.interface import interface
from modules import registers as r
from modules import busses as b
from modules.PCInterfaces import PCInterface
from modules.IOInterfaces import ABH, ABL, DL, DOR, PASS_SBDB, PASS_SBADH
from modules.regX import X
from modules.regY import Y
from modules.accumulator import AC
from modules.alu import ALU
from modules.stackPoint import S
from modules.latch import latch
cSignals = latch()  # need to make cSignals
PCLS = latch()
PCL = latch()
PCHS = latch()
PCH = latch()
flagReg = latch()
PC = PCInterface(PCLS, PCL, PCHS, PCH,
                 b.dataBus, b.addressLowBus, b.addressHighBus, cSignals, name='PC')
ABH = ABH(ABH, cSignals)
ABL = ABL(ABL, cSignals)
DL = DL(ABL, b.dataBus, ABH, b.externalDataBus, cSignals)
DOR = DOR(b.dataBus, b.externalDataBus, cSignals)
PASS_SBDB = PASS_SBDB(b.dataBus, b.specialBus, cSignals)
PASS_SBADH = PASS_SBADH(ABH, b.specialBus, cSignals)
X = X(b.specialBus, cSignals)
Y = Y(b.specialBus, cSignals)
AC = AC(b.dataBus, b.specialBus, cSignals)
BI = latch()
ADD = latch()
AI = latch()
ALU = ALU(AI, BI, ADD, flagReg, cSignals)
S = S(ABL, b.specialBus, cSignals)
