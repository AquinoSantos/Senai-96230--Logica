import os
os.system("clear")

print("Restaurante SENAI\n")

print("Confira nosso cardapio: ")

opcao = int(input("""
 Codigo  \t\t Prato \t\t\t valor
    1   \t\t Picanha \t\t R$ 25,00
    2   \t\t Lasanha \t\t R$ 20,00
    3   \t\t Strogonoff \t\t R$ 18,00
    4   \t\t Bife acebolado \t R$ 15,00
    5   \t\t Pão com ovo \t\t R$ 5,00
                  
Digite a opção desejada: """))

#processamento

match opcao:
    case 1:
        prato = "Picanha"
        valor = 25.00
    case 2:
        prato = "Lasanha"
        valor = 20.00
    case 3:
        prato = "Strogonoff"
        valor = 18.00
    case 4:
        prato = "Bife acebolado"
        valor = 15.00
    case 5:
        prato = "Pão com ovo"
        valor = 5.00
    case _:
        prato = "Opção invalida"
        valor = 0.00
        

#saida
print(f"\nPrato escolhido:  {prato}")
print(f"Valor:  R$ {valor}")

print("\nObrigado pela preferencia!")
print("Volte sempre!")
