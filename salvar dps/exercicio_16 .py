import os
os.system("cls || clear")

media_salario = 0
maior_idade = 0
menor_idade = 0
mulheres_salario = 0
quantidade = 0


while True:

    print("Menu")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

    opcao = input(" O que deseja fazer:")


    
    
    if opcao == "1":

        quantidade = int(input("Digite a quantidade de pessoas:"))
        media_salario = 0
        maior_idade = 0
        menor_idade = 100
        mulheres_salario = 0



        for i in range(quantidade):

            idade = int(input(f"Digite a {i+1}ª idade: "))
            sexo = input("Digite seu sexo(M/F): ").upper()
            salario = float(input(f"Digite o {i+1}º salario:"))


    media_salario += salario

    if idade > maior_idade:

            maior_idade = idade

    if idade < menor_idade:

            menor_idade = idade

    if sexo == "F" and salario >= 5000:
            mulheres_salario += 1

           

    elif opcao == "2":

        media_salario = media_salario / quantidade

        print(f"Media de salario é: {media_salario}")
        print(f"Maior idade do grupo: {maior_idade}")
        print(f"Menor idade do grupo: {menor_idade}")
        print(f"Quantidade de mulheres com salario apartir de R$5000: {mulheres_salario}")

    
    elif opcao == "3":

        break
        
    
        

    


