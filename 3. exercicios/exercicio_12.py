import os
os.system("cls || clear")

opcao = input("""
 Codigo  \t\t Prato \t\t\t valor
    1   \t\t Picanha \t\t R$ 25,00
    2   \t\t Lasanha \t\t R$ 20,00
    3   \t\t Strogonoff \t\t R$ 18,00
    4   \t\t Bife acebolado \t R$ 15,00
    5   \t\t Pão com ovo \t\t R$ 5,00
                  
Digite o numero da opcao desejada:
              """)



opcao = int(input("Digite o número da opção desejada: "))

match opcao:
    case 1:
        prato = "Picanha"
        valor = 25
    case 2:
        prato = "Lasanha"
        valor = 20
    case 3:
        prato = "Strogonoff"
        valor = 18
    case 4:
        prato = "Bife acebolado"
        valor = 15
    case 5:
        prato = "Pão com ovo"
        valor = 5
    case _:
        print("Opção inválida")
        preco = 0

soma += preco
continuar = input("Deseja ecolher outro prato? \nDigite 'S' ou 'N': ").lower()
if continuar == "n":
           
 os.system("cls || clear")

print(f"\nTotal a pagar: R$ {soma}")
