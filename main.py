from mdl import Imub
from vrb import Udvb

# THIS IS JUST A SCRIPT USED FOR TESTING
# SVESS AS PROSTA SKRIPT YRYL TITESTAT

iim =input("")
p = input("")
a = input(str(Imub(iim, "SG").udarath_imy) +"\n" +str(Imub(iim, "PL").udarath_imy) +"\n" +str(Imub(iim, "PA").udarath_imy))
print(Udvb(p))
