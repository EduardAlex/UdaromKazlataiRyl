from mdl import Imub
from mdl import Unsusithiub
from vrb import Udvb

# THIS IS JUST A SCRIPT USED FOR TESTING
# SVESS AS PROSTA SKRIPT YRYL TITESTAT

def inttxt(txt):
    a = ""
    skip = False
    b = {"y'": 'ý', 'a:': 'ä', 'u:': 'ü', 'a.': 'ą', 'e:': 'ë', 'i:': 'ï',
        "t'": 'ť', "d'": 'ď', "s'": 'ś', "z'": 'ź', "h'": 'ħ', "c'": 'ć', "l'": 'ĺ', "n'": 'ń',
        "g'": 'ģ', 'u<': 'ŭ', 'c<': 'č', 'z<': 'ž', 's<': 'š', 't;': "ts'", "a'": "à"}
    for i,j in enumerate(txt):
        if skip:
            skip = False
            continue
        try:
            s = j + txt[i+1]
            if s in b:
                a += b[s]
                skip = True
            else:
                a += j
        except:
            a += j
    return a

# iim =input("")
p = inttxt(input(""))
# a = input("negative?")
# b = input("inter?")
# c = input("subj?")
# a = bool(len(a))
# b = bool(len(b))
# c = bool(len(c))
# # a = input(str(Imub(iim, "SG").udarath_imy) +"\n" +str(Imub(iim, "PL").udarath_imy) +"\n" +str(Imub(iim, "PA").udarath_imy))
# print(Udvb(p, vrm="PRES_PRD",zan=a,vop=b,subj=c))
print(Unsusithiub(p, num="PL"))
