import os
from dataclasses import dataclass

os.system("cls || clear")



@dataclass
class Pessoa:
    nome:str
    idade:int

@dataclass
class pet:
    nome: str
    idade: int
    raca:str


pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = pet("Toto", 4, "Caramelo")
pet2 = pet("Hulk", 6, "Pitbull")


print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}")

print(f"Nome: {pet1.nome}, Idade: {pet1.idade}, Raça: {pet1.raca}")
print(f"Nome: {pet2.nome}, Idade: {pet2.idade}, Raça: {pet2.raca}")

