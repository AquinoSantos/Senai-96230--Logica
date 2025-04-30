import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Endereco:
    logradouro: str
    numero: str



@dataclass
class Pessoa: # Atributo é uma variavel que esta dentro da classe.

    nome: str
    idade:int
    endereco: Endereco

    def exibindo_dados(self):# metodo é uma função que esta dentro da classe.
        print(f"\nNome:{self.nome}\nidade: {self.idade}\nLogradouro: {self.endereco.logradouro}\nNumero: {self.endereco.numero}" )   







endereco1 = Endereco("Rua B", "45")
pessoa1 = Pessoa("Aquino","senai@ba.com", endereco1, "Salvador")





print("Exibindo Dados")
pessoa1.exibindo_dados()