import os
from dataclasses import dataclass

os.system("cls || clear")


@dataclass
class Endereco():

    nome: str
    email:str
    telefone:str
    endereco: str

    def exibindo_dados(self):
        print("Exibindo Dados")
        print(f"\nNome:{self.nome}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}")   


print("\nSolicitando Dados")

nome  = input("\nDigite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")




end1 = Endereco(nome, email, telefone, endereco)
end1.exibindo_dados()




