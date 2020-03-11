import numpy,os,datetime,time

def make(seed=0):
    if seed==0:
        seed=numpy.random.randint(10e7,10e8-1,dtype='int64')
    numpy.random.seed(seed)
    dices=numpy.random.randint(1,7,22)
    STR=dices[0]+dices[1]+dices[2]
    CON=dices[3]+dices[4]+dices[5]
    POW=dices[6]+dices[7]+dices[8]
    DEX=dices[9]+dices[10]+dices[11]
    APP=dices[12]+dices[13]+dices[14]
    SIZ=dices[15]+dices[16]+6
    INT=dices[17]+dices[18]+6
    EDU=dices[19]+dices[20]+dices[21]+3
    SAN=POW*5
    IDEA=INT*5
    LUCK=POW*5
    NLG=EDU*5 #Knowledge
    HP=(CON+SIZ)/2
    MP=POW
    result="\nSTR(筋力):"+str(STR)+"\nCON(体力):"+str(CON)+"\nPOW(精神力):"+str(POW)+"\nDEX(敏捷性):"+str(DEX)+"\nAPP(外見):"+str(APP)+"\nSIZ(体格):"+str(SIZ)+"\nINT(知性):"+str(INT)+"\nEDU(教育):"+str(EDU)+"\nSAN(正気度):"+str(SAN)+"\nIDEA(アイデア):"+str(IDEA)+"\nLUCK(幸運):"+str(LUCK)+"\nNLG(知識):"+str(NLG)+"\nHP(耐久力)"+str(HP)+"\nMP(マジックポイント):"+str(MP)+"\nSeed:D"+str(seed)
    return result

def load(index:str):
    if index[0]=='D':
        seed = index.replace("D","")
        return make(int(seed))
    else:
        return "Invaild format! : " + str(index)    