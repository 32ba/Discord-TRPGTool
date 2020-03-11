import asyncio
from numpy.random import *

def roll(num:int,dice:int,onlysum:bool=False):
    isfumble=False
    iscritical=False
    if num>100:
        return '100個以上のダイスを振ることはできません'
    if dice>100:
        return "ダイスの目を100以上にすることはできません"
    dicesum=0
    roll=str(num)+"D"+str(dice)
    resdetail="("+roll+" : "
    for i in range(num):
        if i != 0:
            resdetail+=","
        d = randint(1,dice+1)
        resdetail+=str(d)
        dicesum+=d
    if num==1 and dice==100:
        if dicesum<=5:
            iscritical=True
        if dicesum>=96:
            isfumble=True
    if onlysum == True:
        return dicesum
    else:
        result=str(dicesum)+" "+resdetail+")"+(" Critical!" if iscritical==True else " Fumble!" if isfumble==True else "")
        return result