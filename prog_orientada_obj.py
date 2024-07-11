class cachorro: 
    def __init__(self, raça, cor, nome, sexo, peso, altura, data_nasc, quant_comida_porcao):
        self.raça = raça
        self.cor = cor
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.data_nasc = data_nasc
        self.quant_comida_porcao = quant_comida_porcao
        self.comida = 500

    def comer(self):
        self.comida -= self.quant_comida_porcao
        print(f"O cachorro {self.nome} comeu, mas ainda tem {self.comida}g de comida.")
        
    def latir(self):
        print(f"O cachorro {self.nome} está latindo!!!")

    def imprimir_info(self):
        print("Raça:",self.raça, "\nCor:",self.cor, "\nNome:",self.nome,
    "Sexo:",self.sexo, "\nPeso:",self.peso, "\nAltura:",self.altura,
    "\nData de nascimento:",self.data_nasc)

if __name__ == '__main__':
    primeiro_cachorro = cachorro("Cofap", "Marrom", "Vina", "Masculino", 5.590, 32.5, "06/03/2006", 150)
    # print(meu_primeiro_cachorro.nome)
    segundo_cachorro = cachorro("SRD - caramelo", "caramelo", "Thor", "marc", 5, 5, 5, 200)
    # primeiro_cachorro.latir()
    # segundo_cachorro.comer()
    # primeiro_cachorro.comer()
    primeiro_cachorro.imprimir_info()