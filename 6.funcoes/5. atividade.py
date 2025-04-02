#faça uma função sem retorno com o nome: logo_senai()
# limpando o terminal, e inserindo: ===SENAI DENDEZEIROS ===
 
#Solicite ao usuario dois numeros
# Cada um em uma variavel diferente
# Crie uma função para somar os dois numeros informados pelo usuario


import os


def logo_senai():
 os.system("cls || clear")   
 print(" === SENAI DENDEZEIROS === ") 


def somar(n1, n2):
 return n1 + n2

logo_senai()
n1 = int(input("Digite o primeiro numero:"))

logo_senai()
n2 = int(input("Digite o segundo numero:"))

soma = somar(n1, n2)


logo_senai()  # chamando a função

print(f"Soma: {soma}")


