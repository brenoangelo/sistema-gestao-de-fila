import os

op = 0
op2 = 0
codc = 0
codv = 0
n = 0
#con = []
#pref = []

fila = []


os.system('cls')
while(op2 != 5):

    print('SISTEMA DE GESTAO DE FILAS-SGF')
    print('\n')
    print('Informe o tipo de atendimento')
    print('\n')
    op = int(input('''
        Selecione uma opção:
        - [1] Convencional
        - [2] Prioridade \n 
        '''))
    print('\n')

    op2 == 0
    print("Informe o setor para o atendimento")
    op2 = int(input('''
            Selecione uma opção:
            - [1] Caixa
            - [2] Guiche
            - [3] Gerencia
            - [4] Acompanhamento
            - [5] Sair \n 
            '''))
    os.system('cls')
    if op2 == 1:
        #Caixa
        print("Caixa")
        
        if op == 1:
            codc += 1
            fila.append(('{}{}'.format("CXC", codc)))
        elif op == 2:
            codv += 1
            fila.append(('{}{}'.format("CXP", codv)))
        
    elif op2 == 2:
        #Guichê
        print("Guiche")

        if op == 1:
            codc += 1
            fila.append(('{}{}'.format("CHC", codc)))
            
        elif op == 2:
            codv += 1
            fila.append(('{}{}'.format("GHP", codv)))
        
    elif op2 == 3:
        #Gerencia
        print("Gerencia")

        if op == 1:
            codc += 1
            fila.append(('{}{}'.format("GEC", codc)))
        elif op == 2:
            codv += 1
            fila.append(('{}{}'.format("GEP", codv)))

    elif op2 == 4:
        print("Acompanhamento")
        print("\n")
        for i in fila:
            n = n + 1
            print("Caixa:",n ,"Senha:",i,"\n")
        

        #for i in con:
        #    index = +con.index(i)
        #    print("Senha: ",i)
        #    print("Caixa: ",index)
            
        #for i in pref:
        #    index = +pref.index(i)
        #    print("Senha: ",i)
        #    print("Caixa:",index)