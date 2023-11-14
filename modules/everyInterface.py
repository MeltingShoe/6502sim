from modules.interface import interface
from modules import registers as r
from modules import busses as b
from modules.PCInterfaces import PCInterface


PC = PCInterface(r.PCLSReg, r.PCLReg, r.PCHSReg, r.PCHReg,
                 b.dataBus, b.addressLowBus, b.addressHighBus, name='PC')
