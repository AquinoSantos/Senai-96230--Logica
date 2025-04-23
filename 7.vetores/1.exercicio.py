import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 6
lista_numeros = []
pares = 0
impares = 0

for i in range (QUANTIDADE_NUMEROS):

    numero = int(input(f"Digite o {i + 1}º número: "))

    lista_numeros.append(numero)
    if numero % 2 == 0:

        pares += 1
    else:
        impares += 1


print(f"\nA lista de números é: {lista_numeros}")

print(f"numeros informados: {QUANTIDADE_NUMEROS}")

print(f"A quantidade de números pares é: {pares}")

print(f"A quantidade de números ímpares é: {impares}")
