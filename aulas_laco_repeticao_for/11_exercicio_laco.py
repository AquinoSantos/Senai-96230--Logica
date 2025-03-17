import os
os.system("cls || clear")

soma = 0

for i in range(3):
    
    nota = float(input(f"Digite a {i+1}ª nota: "))

    soma = soma + nota

    media = soma / 3

if media >= 7:
    print(f"A media é: {media}")
    print("Voce esta aprovado!")

elif media >= 4:
    print(f"A media é: {media}")
    print("Voce esta em recuperação!")

elif media < 4:
    print(f"A media é: {media}")
    print("Voce esta reprovado!")

else:
    print("Erro no resultado!")



print("FIM DO PROGRAMA")
