
import os
os.system("Clear || cls")


# Algoritmo para verificar se um empregado pode ou não se aposentar
#idade e tempo de trabalho minimo.
#solicitar matricula(codigo), ano de nascimento e tempo de trabalho em anos.
#escrever codigo do empregado, idade, tempo de trabalho e mensagem "Requerer aposentadoria" ou "Não requerer aposentadoria"

matricula = (input("Digite sua matricula (codigo): "))

nascimento = int(input("Digite seu ano de nascimento : "))

tempo_trabalhado = int(input("Digite seu tempo de trabalho(anos): "))

print("")

ano = 2025

idade = ano - nascimento


if idade >= 65 or tempo_trabalhado >= 30:
    print(f"Matricula: {matricula}")
    print(f"Idade: {idade}")
    print(f"Tempo de trabalho: {tempo_trabalhado} anos")
    print("Requerer Aposentaria")

else:

    print(f"Matricula: {matricula}")
    print(f"Idade: {idade}")
    print(f"Tempo de trabalho: {tempo_trabalhado} anos")
    print("Não Requerer Aposentadoria")














































































































































