import os
os.system("cls || clear")


soma = 0
contador = 1

while True:

    nota = float(input("Digite uma nota: "))
    continuar = input("Deseja inserir outra nota? (s/n): ").upper()
    if continuar == 'N':
     break


    else:

     soma += nota
     contador += 1

   
    if contador == 0:
        soma = nota
        contador = 1
        

media = soma / contador
print(f"\nA média das notas é: {media}")

















