import os
os.system("cls || clear")


cont = 0



while True:
    #comandos a serem repetidos
    print("Repetindo...")

    continua = input("Tecle 's' se desejar continuar: ").strip().lower()
    cont+=1

    if continua != 's':
        break

if cont == 0:
        print("O bloco NÃO foi repetido.")
else:
        print(f"O bloco foi repetido {cont} vezes ")

