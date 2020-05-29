import random

letrasg=['Q','E','R','P','A','D','F','G','B','N','M']
letrasp=['q','e','r','p','a','d','f','g','b','n','m']
simbolos=['!','§','$','%','&','/','(',')','=','+','*','#','-','_','.',':',',',';','<','>']
numeros=['1','2','3','4','5','6','7','8','9','0']



quantaspass= int(input('Quantas passwords para gerar:'))

comprimento=int(input('Quantos Carateres:'))

for i in range (1,quantaspass):

    password=''

    for i in range (1,comprimento):
        tipo=random.randint(1,4)
        if tipo==1:
            password +=random.choice(letrasg)
        if tipo==2:
            password +=random.choice(letrasp)
        if tipo==3:
            password +=random.choice(simbolos)
        if tipo==4:
            password +=random.choice(numeros)

    print(password)