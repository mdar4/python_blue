class Pessoa:
    def __init__(self, nome, idade, peso):
        self.nomePessoa = nome
        self.idadePessoa = idade
        self.pesoPessoa = peso

    def comer(self, calorias):
        if self.idadePessoa > 30:
            self.pesoPessoa +=  calorias * 2
        else:
            self.pesoPessoa += calorias

    def malhar(self, calorias):
        if self.idadePessoa <= 30:
            self.pesoPessoa -= calorias * 2
        else:
            self.pesoPessoa -= calorias

    def dados(self):
        return f''''
            Nome = {self.nomePessoa}
            Idade = {self.idadePessoa}
            Peso = {self.pesoPessoa}
        
        '''


pessoa1 = Pessoa('Dara', 20, 45.9)
pessoa2 = Pessoa('José', 34, 76.6)

pessoa1.comer(3)
pessoa2.malhar(6)

print(pessoa1.dados())
print(pessoa2.dados())