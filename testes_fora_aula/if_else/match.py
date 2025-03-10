import os
os.system("clear")


nome = input("Digite seu nome: ").upper()
nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))

soma = nota_um + nota_dois
media = soma / 2

conceito = "A", "B", "C", "D", "E"




if media >= 9:

   conceito = "A"

elif media >= 7.5 and media < 9:

    conceito = "B"

elif media >= 6 and media < 7.5:
    
    conceito = "C"     

elif media >= 4 and media < 6:

    conceito = "D"

elif media < 4 and media > 1:

    conceito = "E"


else:
    print("Erro ao processar dados, digite os dados corretamente")


match conceito:

    case "A"| "B"| "C" :
        print(f"Conceito : {conceito} ")
        print("Aprovado")


    case "D"| "E":
        print(f"Conceito : {conceito} ")
        print("Reprovado")    


    case _:

        print("Opçao invalida ")  
     