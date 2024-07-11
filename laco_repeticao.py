# for i in range(int(input("Digite quantas vezes deseja repetir.\nR: "))):
#     print(i)

# nomes = ["Daniel", "Carlos", "Flávio", "Gabrielly"]

# for nome in nomes:
#     print(nome)

valor = ""

while valor != "sair":
    #valor = int(input("Digite um valor.\n-R: "))
    
    valor = input("Digite algo.\n-R: ")
    if valor != "sair":
        valor = int(valor)