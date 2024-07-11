import os
contador_saque = 0
contador_deposito = 0
opcao = 99
lista_valor_saque = []
lista_valor_deposito = []

def menu():
    
    print("==================\n| (1) - Extrato  |\n| (2) - Saque    |")
    print("| (3) - Depósito |\n| (0) - Sair     |\n==================")

def saque():
    global saldo, contador_saque
    print("- Saque -")
    valor_saque = float(input("\n-Digite o valor desejado do saque ou pressione zero (0) para retornar.\n-R: "))

    if valor_saque == 0:
        inicio()
    elif valor_saque <= saldo and valor_saque > 0:
        saldo = saldo - valor_saque
        contador_saque += 1
        lista_valor_saque.append(valor_saque)
        print(f"Você fez um saque de R${valor_saque} .Saldo disponível: R${saldo}\n")
    else:
        print("-Saldo indisponível ou valor de saque inválido.")
        saque() 

def deposito():
    global saldo, contador_deposito
    print("- Depósito -")
    valor_deposito = float(input("\n-Digite o valor desejado do depósito ou pressione zero (0) para retornar.\n-R: "))
    if valor_deposito > 0:
        saldo = saldo + valor_deposito
        contador_deposito += 1
        lista_valor_deposito.append(valor_deposito)
        print(f"Você fez um depósito de R${valor_deposito} .Saldo disponível: R${saldo}\n")
    elif valor_deposito == 0:
        inicio()
    else:
        print("Valor de depósito inválido.")

def extrato():
    print(f"====================================\n| -Nome: {nome}\n| -Saldo atual: R${saldo}")
    print(f"| -Quantidade de saques: {contador_saque} \n| -Quantidade de depósitos: {contador_deposito}")
    if(len(lista_valor_saque) > 0):
        ultimo = lista_valor_saque[-1]
    else:
        ultimo = 0.0
    print(f"| -Valor do último saque: R${ultimo} ")
    if(len(lista_valor_deposito) > 0):
        ultimo = lista_valor_deposito[-1]
    else:
        ultimo = 0.0
    print(f"| -Valor do último depósito: R${ultimo}")
    print("====================================")

def ler_variavel():
    if opcao == "1":
        extrato()
    elif opcao == "2":
        saque() 
    elif opcao == "3":
        deposito()
    if opcao == "0":
        inicio()
    else:
        print("Selecione uma opção válida.")

def inicio():
    global opcao
    while opcao != "0":
        menu()
        opcao = (input("-R: "))
        os.system("cls")
        ler_variavel()
nome = input("Digite seu nome.\n-R: ")
saldo = float(input("Digite o saldo da conta.\n-R: "))
inicio()