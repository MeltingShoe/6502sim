from modules.interface import interface
from modules import registers as r
from modules import busses as b
from modules.PCInterfaces import PCInterface

PC = PCInterface(name='PC')
DL_DB = interface(r.inputDataReg, b.dataBus, name='DL-DB')
DL_ADL = interface(r.inputDataReg, b.addressLowBus, name='DL-ADL')
DL_ADH = interface(r.inputDataReg, b.addressHighBus, name='DL-ADH')

S_SB = interface(r.stackPointReg, b.specialBus, name='S-SB')
S_ADL = interface(r.stackPointReg, b.addressLowBus, name='S-ADL')
ABH_ADH = interface(r.ABHReg, b.addressHighBus, name='ABH-ADH')
ABL_ADL = interface(r.ABHReg, b.addressLowBus, name='ABL-ADL')
BI_DB = interface(r.bInReg, b.dataBus, name='BI_DB')
BI_ADL = interface(r.bInReg, b.addressLowBus, name='BI-ADL')
AI_SB = interface(r.aInReg, b.specialBus, name='AI-SB')
AC_DB = interface(r.acc, b.dataBus, name='AC-DB')
AC_SB = interface(r.acc, b.dataBus, name='AC-SB')
P_DB = interface(r.flagReg, b.dataBus, name='P-DB')
Y_SB = interface(r.regY, b.specialBus, name='Y-SB')
X_SB = interface(r.regX, b.specialBus, name='X-SB')
DOR_DB = interface(r.dataOutputReg, b.dataBus, name='DOR-DB')
