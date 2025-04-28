import os
from dataclasses import dataclass

os.system("cls || clear")


@dataclass
class Endereco:

    nome: str
    email:str
    telefone:int
    endereco: str


print("Solicitando Dados")

nome  = input("\nDigite seu nome: ")
email = input("Digite seu email: ")
telefone = int(input("Digite seu telefone: "))
endereco = input("Digite seu endereço: ")




end1 = Endereco(nome, email, telefone, endereco)



print(f"\nNome:{end1.nome}\nEmail: {end1.email}\nTelefone: {end1.telefone}\nEndereço: {end1.endereco}")
