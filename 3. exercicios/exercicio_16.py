import os
os.system("cls || clear")

media_salario = 0
maior_idade = 0
menor_idade = 100 
mulheres_salario = 0
quantidade = 0

while True:

    opcao = input("""
    Codigo\t\tMenu
    1\t\tAdicionar pessoa
    2\t\tExibir resultados
    3\t\tSair

    O que deseja fazer: """)

    match opcao:

        case "1":  
            quantidade = int(input("Digite a quantidade de pessoas: "))
            
            for i in range(quantidade):  

                idade = int(input(f"Digite a {i+1}ª idade: "))
                sexo = input("Digite seu sexo(M/F): ").upper()
                salario = float(input(f"Digite o {i+1}º salario: "))

                media_salario += salario

                if idade > maior_idade:
                    maior_idade = idade

                if idade < menor_idade:
                    menor_idade = idade

                if sexo == "F" and salario >= 5000:
                    mulheres_salario += 1

            os.system("cls || clear")  

        case "2":  

            if quantidade > 0:

                media_salario = media_salario / quantidade
                print(f"Media de salario é: {media_salario:.2f}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salario a partir de R$5000: {mulheres_salario}")

            else:
                print("Nenhuma pessoa foi cadastrada ainda.")

        case "3":  
            
            break  

        case _:  
            print("Opção inválida. Tente novamente.")
    
    