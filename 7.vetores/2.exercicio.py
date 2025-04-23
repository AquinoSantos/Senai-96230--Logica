import os
os.system("cls || clear")


print("Restaurante SENAI")

opcao = print(

    """Menu\tProduto\t\t\tValor
 1 - \tLasanha......... \tR$ 35,00
 2 - \tPizza........... \tR$ 40,00
 3 - \tHambúrguer...... \tR$ 25,00
 4 - \tSushi........... \tR$ 50,00
 5 - \tSalada.......... \tR$ 20,00
 6 - \tBife à Parmegiana\tR$ 30,00
 7 - \tFrango Grelhado. \tR$ 28,00
 0 - \tpara encerrar o pedido""")


subtotal = 0
pedidos = ""
continuar = True
lista_pedidos = []

while continuar:
    
        codigo = int(input("\nDigite o código do prato desejado: "))
        lista_pedidos.append(codigo)

        

        if codigo == 1:
            subtotal += 35.00
            pedidos += "Lasanha (R$ 35,00)\n"
            print("\nPrato 'Lasanha' adicionado ao pedido.")
            

        elif codigo == 2:
            subtotal += 40.00
            pedidos += "Pizza (R$ 40,00)\n"
            print("\nPrato 'Pizza' adicionado ao pedido.")

        elif codigo == 3:
            subtotal += 25.00
            pedidos += "Hambúrguer (R$ 25,00)\n"
            print("\nPrato 'Hambúrguer' adicionado ao pedido.")

        elif codigo == 4:
            subtotal += 50.00
            pedidos += "Sushi (R$ 50,00)\n"
            print("\nPrato 'Sushi' adicionado ao pedido.")

        elif codigo == 5:
            subtotal += 20.00
            pedidos += "Salada (R$ 20,00)\n"
            print("\nPrato 'Salada' adicionado ao pedido.")

        elif codigo == 6:
            subtotal += 30.00
            pedidos += "Bife à Parmegiana (R$ 30,00)\n"
            print("\nPrato 'Bife à Parmegiana' adicionado ao pedido.")

        elif codigo == 7:
            subtotal += 28.00
            pedidos += "Frango Grelhado (R$ 28,00)\n"
            print("\nPrato 'Frango Grelhado' adicionado ao pedido.")

        elif codigo == 0:
            continuar = False

        else:
            print("\nCódigo inválido. Por favor, escolha um código válido.")
    
        

if subtotal > 0:
    
    print("\n--- Pedido Finalizado ---")
    print("Pratos escolhidos:")
    print(pedidos)
    print(f"Subtotal: R$ {subtotal:.2f}")

    while True:
        forma_pagamento = input("\nEscolha a forma de pagamento (1- À vista / 2- Cartão de Crédito): ")

        if forma_pagamento in ["1", "2"]:
            break

        else:
            print("Opção inválida. Escolha '1' ou '2'.")

    if forma_pagamento == "1":
        desconto = subtotal * 0.10
        total = subtotal - desconto
        print("\nForma de pagamento: À vista")
        print(f"Desconto aplicado: R$ {desconto:.2f}")

    elif forma_pagamento == "2":
        acrescimo = subtotal * 0.10
        total = subtotal + acrescimo
        print("\nForma de pagamento: Cartão de Crédito")
        print(f"Acréscimo aplicado: R$ {acrescimo:.2f}")

    print(f"Total a pagar: R$ {total:.2f}")

    print(f"Codigos escolhidos: {lista_pedidos}")
    
else:
    print("\nNenhum prato foi selecionado. Pedido encerrado.")