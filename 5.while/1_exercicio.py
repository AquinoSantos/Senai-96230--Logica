import os
os.system("cls || clear")


while True:

    nota = float(input("Digite a nota: "))

    if nota < 0 or nota > 10:

       nota = int(input("Digite a nota: "))

    else:

        print(f"A nota informada foi: {nota} ")

        break

print("FIM")