import os
os.system("clear")

nome = str(input("Digite seu nome: "))

idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f"Olá {nome}, infelizmente você não esta apto a votar .")

elif idade >= 16 and idade == 17:
    print(f"Olá {nome},você pode votar, mas não é obrigatório.")

elif idade >= 18 and idade <= 65:
    print(f"Olá {nome},seu voto é obrigatório.")

elif idade > 65:
    print(f"Olá {nome},você pode votar, mas não é obrigatório.")


print("==FIM==")


