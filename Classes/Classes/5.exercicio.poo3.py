import os
from dataclasses import dataclass
os.system("cls || clear")


@dataclass
class Sub_dados:
    logradouro: str
    numero: int



@dataclass
class Dados:
    nome: str
    email: str
    endereco: str
    cidade: str




    def exibindo_dados(teste):

        print(f"\nNome: {teste.nome}\nEmail: {teste.email}\nEndereço: {teste.endereco.logradouro}\nNumero: {teste.endereco.numero}\nCidade: {teste.cidade}")
        
nome  = input("\nDigite seu nome: ")
email = input("Digite seu email: ")
logradouro = input("Digite seu endereço: ")
numero = int(input("Digite o número: "))
cidade = input("Digite sua cidade: ")






endereco = Sub_dados(logradouro=logradouro, numero=numero)
sub_endereco = Dados(nome=nome, email=email, endereco=endereco, cidade=cidade)


print("Exibindo Dados")
sub_endereco.exibindo_dados()




