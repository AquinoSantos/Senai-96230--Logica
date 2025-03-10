import os
os.system("clear")


nome = input("Digite seu nome: ").upper()
nota_um = float(input("Digite a primeira nota: "))
nota_dois = float(input("Digite a segunda nota: "))


media = (nota_um + nota_dois) / 2


if media >= 9:

    print(f"Nome: {nome}")
    print(f"Nota 1: {nota_um}")
    print(f"Nota 2: {nota_dois}")
    print(f"Media: {media:.2f}")
    print("Conceito: A")
    print("Aprovado!")

elif media >= 7.5 and media < 9:

    print(f"Nome: {nome}")
    print(f"Nota 1: {nota_um}")
    print(f"Nota 2: {nota_dois}")
    print(f"Media: {media:.2f}")
    print("Conceito: B")
    print("Aprovado!")

elif media >= 6 and media < 7.5:
    
    print(f"Nome: {nome}")
    print(f"Nota 1: {nota_um}")
    print(f"Nota 2: {nota_dois}")
    print(f"Media: {media:.2f}")
    print("Conceito: C")
    print("Aprovado!")        

elif media >= 4 and media < 6:

    print(f"Nome: {nome}")
    print(f"Nota 1: {nota_um}")
    print(f"Nota 2: {nota_dois}")
    print(f"Media: {media:.2f}")
    print("Conceito: D")
    print("Reprovado!")    

elif media < 4 and media > 1:

    print(f"Nome: {nome}")
    print(f"Nota 1: {nota_um}")
    print(f"Nota 2: {nota_dois}")
    print(f"Media: {media:.2f}")
    print("Conceito: E")
    print("Reprovado!")


else:
    print("Erro ao processar dados, digite os dados corretamente")


           