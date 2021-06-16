import os
from datetime import datetime

op = 0
op2 = 0
codc = 0
codv = 0
n = 0
tipo = ""
filaCurrent = ""
area = ""

senha1 = ""
senha2 = ""
senha3 = ""
senha1pref = ""
senha2pref = ""
senha3pref = ""

senhaprefixo = ""

fila = []

def ticket(prefixo, current):
    
    #prefixo = i[0:2]
    
    if prefixo == "CXC":
        tipo = "Convencional"
    elif prefixo == "CXP":
        tipo = "Preferencial"

    elif prefixo == "GHC":
        tipo = "Convencional"
    elif prefixo == "GHP":
        tipo = "Preferencial"

    elif prefixo == "GEC":
        tipo = "Convencional"
    elif prefixo == "GEP":
        tipo = "Preferencial"

    print("======================\n")
    print("SISTEMA DE GESTAO DE FILAS")
    print("======================\n")
    print("BANCO NOSSO CREDITO\n")
    print("Av. Principal N 100, Centro\n")
    print("fone (86) 9-6115-1368\n")
    print(".....................\n")
    print("SENHA: ",current,"\n")
    print("Tipo: ", tipo,"\n")
    print("Data: ",datetime.now().strftime('%d-%m-%Y'),"\n")
    print("Hora: ",datetime.now().strftime('%H:%M'),"\n")

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
            filaCurrent = ('{}{}'.format("CXC", codc))
            ticket("CXC", filaCurrent)
        elif op == 2:
            codv += 1
            
            fila.append(('{}{}'.format("CXP", codv)))
            filaCurrent = ('{}{}'.format("CXP", codv))
            ticket("CXP", filaCurrent)
        
    elif op2 == 2:
        #Guichê
        print("Guiche")

        if op == 1:
            codc += 1
            fila.append(('{}{}'.format("GHC", codc)))
            filaCurrent = ('{}{}'.format("GHC", codc))
            ticket("GHC", filaCurrent)
            
        elif op == 2:
            codv += 1
            fila.append(('{}{}'.format("GHP", codv)))
            filaCurrent = ('{}{}'.format("GHP", codv))
            ticket("GHP", filaCurrent)
        
    elif op2 == 3:
        #Gerencia
        print("Gerencia")

        if op == 1:
            codc += 1
            fila.append(('{}{}'.format("GEC", codc)))
            filaCurrent = ('{}{}'.format("GEC", codc))
            ticket("GEC", filaCurrent)
        elif op == 2:
            codv += 1
            fila.append(('{}{}'.format("GEP", codv)))
            filaCurrent = ('{}{}'.format("GEP", codv))
            ticket("GEP", filaCurrent)

    elif op2 == 4:
        for i in fila:
            area = i[0:2]
            senhaprefixo = i[1:3]
            if area == "CX":
                
                if senhaprefixo == "P":
                    senha1pref = i
                senha1 = i
            elif area == "GH":
                
                if senhaprefixo == "P":
                    senha1pref = i
                senha2 = i
            elif area == "GE":
                if senhaprefixo == "P":
                    senha1pref = i
                senha3 = i
            
            n = n + 1
            os.system('cls')
            print("PAINEL DE ACOMPANHAMENTO\n")
            print("Senha:",senha1,"\n")
            print("Caixa:",n,"\n\n")

            print("Senha:",senha2,"\n")
            print("Guiche:",n,"\n\n")

            print("Senha:",senha3,"\n")
            print("Gerencia:",n,"\n\n")

            print("Senha:",senha1pref,"\n")
            print("Caixa:",n,"\n\n")

            print("Senha:",senha2pref,"\n")
            print("Guiche:",n,"\n\n")

            print("Senha:",senha3pref,"\n")
            print("Gerencia:",n,"\n\n")  