#nome = input("Digite o nome do aluno.\n-R: ")
notas = []

def ler_nota():
    notas.append(float(input("Digite uma nota.\n-R: ")))

def calcular_media():
    somatorio = sum(notas)
    quant_notas = len(notas)
    media = somatorio / quant_notas
    print(round(media,2))

ler_nota()
ler_nota()
ler_nota()
ler_nota()
calcular_media()
print(max(notas))
print(min(notas))




# notas.append(7.5)
# notas.append(8.5)
# notas.append(3.5)
# print(notas)

# notas.pop()
# print(notas)

# notas.append(10)
# notas.append(14)
# print(notas)

# notas.pop(0)
# print(notas)
# print(len(notas))

# notas[0] = 12
# print(notas)
# print(len(notas))