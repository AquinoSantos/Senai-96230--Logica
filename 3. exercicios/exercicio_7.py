import os
os.system("clear")

idade = int(input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("Seu voto é opcional.")
else:
    print("Seu voto é obrigatorio.")




print(f"Você tem {idade} anos.")
print("Fim")