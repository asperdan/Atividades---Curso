import os
class Pessoa:

    def __init__(self, nome="", sexo="", cpf="", ano_nasc=0, salario_bruto=0.0):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.salario_bruto = salario_bruto
        self.ano_nasc = ano_nasc
        self.idade = self.calcular_idade() 
        self.salario_liquido = self.calcular_salario_liquido()     
        self.desconto = (self.calcular_inss() + self.calcular_innf())

    def calcular_idade(self):
        return 2024 - self.ano_nasc

    def imprimir_info(self):
        print(f"---INFORMAÇÕES---\nNome: {self.nome}\nCPF: {self.cpf}\nSexo: {self.sexo}")
        print(f"Salário bruto: {round(self.salario_bruto,2)}\nSalário líquido: {round(self.salario_liquido, 2)}")
        print(f"(\nValor do desconto: {round(self.desconto, 2)}")

    def calcular_salario_liquido(self):
        return self.salario_bruto - (self.calcular_innf() + self.calcular_inss())

    def calcular_innf(self):
        salario = self.salario_bruto
        if salario < 2259.21:
            return 0
        elif salario >= 2259.21 and salario <= 2826.65:
            return self.calcular_porcentagem(7.5)
        elif salario > 2826.65 and salario <= 3751.05:
            return self.calcular_porcentagem(15.00)
        elif salario >3751.05 and salario <= 4664.68:
            return self.calcular_porcentagem(22.5)
        elif salario > 4664.68:
            return self.calcular_porcentagem(27.5)
        else:
            return 0.0

    def calcular_inss(self):
        salario = self.salario_bruto
        if salario < 1412.00:
            return self.calcular_porcentagem(7.5)
        elif salario > 1412.00 and salario <= 2666.68:
            return self.calcular_porcentagem(9.00)
        elif salario > 2666.68 and salario <= 4000.03:
            return self.calcular_porcentagem(12.00)
        else:
            return self.calcular_porcentagem(14.00)
            
    def calcular_porcentagem(self, porcentagem):
        return (self.salario_bruto * porcentagem) / 100    
    
if __name__ == '__main__':
    # primeira_pessoa = Pessoa("Daniel Spercoski", "Masculino", "123.456.789-01", 2006, 1999.37)
    #segunda_pessoa = Pessoa("Gabrielly Ferreira", "Feminino", "109.876.543-21", 2006, 2500.00)
    terceira_pessoa = Pessoa()
    # primeira_pessoa.imprimir_info()
    # print(f"Idade: {primeira_pessoa.idade}")
    # print("-----------------------------")
    #segunda_pessoa.imprimir_info()
    #print(f"Idade: {segunda_pessoa.idade}")
    terceira_pessoa.nome = input("Digite seu nome.\n-R: ")
    terceira_pessoa.cpf = input("Digite seu CPF.\n-R: ")
    terceira_pessoa.sexo = input("Digite seu sexo.\n-R: ")
    terceira_pessoa.ano_nasc = int(input("Digite seu ano de nascimento.\n-R: "))
    terceira_pessoa.salario_bruto = float(input("Digite seu salário bruto.\n-R: "))
    terceira_pessoa.salario_liquido = terceira_pessoa.calcular_salario_liquido()
    terceira_pessoa.idade = terceira_pessoa.calcular_idade()
    terceira_pessoa.imprimir_info()
    #desconto está zerando - arrumar

