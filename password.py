import random

letrasg=['Q','E','R','P','A','D','F','G','B','N','M']
# na proxima defenir  palavra por letra ex b=Beta defletra=[]
letrasp=['q','e','r','p','a','d','f','g','b','n','m']
simbolos=['!','§','$','%','&','/','(',')','=','+','*','#','-','_','.',':',',',';','<','>']
numeros=['1','2','3','4','5','6','7','8','9']



quantaspass= int(input('Quantas passwords para gerar:'))

comprimento=int(input('Quantos Carateres:'))
#
# REGRAS minimu 1 Maiscula, 1 Minuscula, 1 numero, 1 Simbolo

fpass=0

while fpass < quantaspass:

    password=''
    mais=0
    minu=0
    simb=0
    num=0
    

    for j in range (1,comprimento+1
    ):
        tipo=random.randint(1,4)
        if tipo==1:
            password +=random.choice(letrasg)
            mais +=1
        if tipo==2:
            password +=random.choice(letrasp)
            minu +=1
        if tipo==3:
            password +=random.choice(simbolos)
            simb +=1
        if tipo==4:
            password +=random.choice(numeros)
            num +=1
        #print(mais,minu,num,simb)
    if mais>0 and minu>0 and simb>0 and num>0:
        fpass +=1
        print(password)

