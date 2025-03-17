import os
os.system("cls||clear")
import time

numero = int(input("Digite um numero: "))

print("Contagem regressiva\n")

for i in range(numero,0,-1):
    print(f"Valor da variavel i: {i}")
    time.sleep(1)

print("FIM DO PROGRAMA")



