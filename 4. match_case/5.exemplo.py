import os
os.system("clear")


produto = float(input("Informe o valor do produto: "))
print("\nForma de pagamento:")
print("\n1 - À vista")
print("2 - A prazo\n")
forma_pagamento = int(input("Escolha a forma de pagamento: "))

if forma_pagamento == 1:

    desconto = produto * 0.10

    total_a_pagar = produto - desconto
    print(f"Valor do produto: R${produto}")
    print("Forma de pagamento: À vista")
    print(f"Valor do desconto: R${desconto}")
    print(f"Total a pagar: R${total_a_pagar}")

elif forma_pagamento == 2:
    parcelas = int(input("Digite a quantidade de parcelas (até 6 vezes): "))

    if parcelas > 6:
        print("Quantidade de parcelas não permitido, o maximo são 6 parcelas.")
    else:
        valor_parcela = produto / parcelas
        print(f"Valor do produto: R${produto}")
        print("Forma de pagamento: A prazo")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor da parcela: R${valor_parcela}")
        print(f"Total a pagar: R${produto}")

else:
    print("Forma de pagamento invalida.")



