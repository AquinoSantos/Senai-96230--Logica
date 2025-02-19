import os
os.system("clear")

nota_um = float(input("Digite a primeira nota:"))
nota_dois= float(input("Digite a segunda nota:"))
nota_tres = float(input("Digite a terceira nota:"))

soma = nota_um + nota_dois + nota_tres
media = soma / 3


print(f"Média: {media}")


if soma >= 7:
    print("Aprovado")

else:
    print("Reprovado")

