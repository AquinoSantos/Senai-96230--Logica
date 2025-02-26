import os
os.system("clear")


dia = input("Digite o dia da semana: ")

match dia:
    case "Segunda":
        print("Hoje é Segunda-feira.")
    case "Terça":
        print("Hoje é Terça-feira.")
    case "Quarta":
        print("Hoje é Quarta-feira.")
    case "Quinta":
        print("Hoje é Quinta-feira.")
    case "Sexta":
        print("Hoje é Sexta-feira.")
    case "Sábado" | "Domingo":
        print("Hoje é fim de semana.")
    case _:
        print("Dia inválido.")

print(dia)

print("===Fim===")

    