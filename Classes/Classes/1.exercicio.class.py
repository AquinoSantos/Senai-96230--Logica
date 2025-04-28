import os

from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Teste:
    nome: str
    idade:int
    peso:float
    altura: float


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))



teste1 = Teste(nome=nome, idade=idade, peso=peso, altura=altura)
teste2 = Teste(nome, idade, peso, altura)


print(f"Nome:{teste1.nome}\nIdade: {teste1.idade}\nPeso: {teste1.peso}\nAltura: {teste1.altura}")
print(f"Nome:{teste2.nome}\nIdade: {teste2.idade}\nPeso: {teste2.peso}\nAltura: {teste2.altura}")
