# To do
# Criar tela inicial com os botões "convencinal" / "preferencial"

import os

op = 0
op2 = 0
cod = 0

con = []
pref = []

os.system('cls')
while(op2 != 5):

    print('SISTEMA DE GESTAO DE FILAS-SGF')
    print('\n')
    print('Informe o tipo de atendimento')
    print('\n')
    op = int(input('1- Convencional | 2- Preferencial\n'))
    print('\n')


    op2 == 0
    print("Informe o setor para o atendimento")
    op2 = int(input("1- Caixa | 2- Guiche\n3- Gerencia | 4- Acompanhamento | 5-SAIR\n"))
    os.system('cls')
    if op2 == 1:
        #Caixa
        print("Caixa")
        
        if op == 1:
            cod += 1
            con.append('{}{}'.format("CXC", cod))
        elif op == 2:
            cod += 1
            pref.append('{}{}'.format("CXP", cod))
        
    elif op2 == 2:
        #Guichê
        print("Guiche")
    elif op2 == 3:
        #Gerencia
        print("Gerencia")
    elif op2 == 4:
        #Acompanhamento
        for i in con:
            print("conv: "+i+con.index(i))
            
        for i in pref:
            print("pref: "+i)
    