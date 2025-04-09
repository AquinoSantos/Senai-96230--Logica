import os


def logo_senai():
 os.system("cls || clear")   
 print(" === SENAI DENDEZEIROS === ") 


def somar(n1, n2):
 return n1 + n2

def subtrair(n1, n2):
 return n1 - n2

def multiplicar(n1, n2):
 return n1 * n2

def dividir(n1, n2):
 return n1 / n2



logo_senai()
n1 = int(input("Digite o primeiro numero:"))

logo_senai()
n2 = int(input("Digite o segundo numero:"))

soma = somar(n1, n2)
sub = subtrair(n1, n2)
multi = multiplicar(n1, n2)
div = dividir(n1, n2)


logo_senai()  # chamando a função

print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {multi}")
print(f"Divisão: {div:.0f}")
print(f"Numeros informados: {n1} e {n2}")