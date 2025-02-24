import os
os.system("clear")


# Solicita ao usuário dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Exibe os dois números informados
print(f"Os números informados foram: {num1} e {num2}")


menor = min(num1, num2)
maior = max(num1, num2)

if num1 == num2:
    print("Os números são iguais.")

else:
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}") 

