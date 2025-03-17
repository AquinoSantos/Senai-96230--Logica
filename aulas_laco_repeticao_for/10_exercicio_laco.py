import os
os.system("cls || clear")


soma = 0

for i in range(4):
    
    nota = float(input(f"Digite a {i+1}ª nota: "))

    soma = soma + nota

    media = soma / 4


print(f"A media é: {media}")

print("FIM DO PROGRAMA")
