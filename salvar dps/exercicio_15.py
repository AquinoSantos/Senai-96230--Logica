import os
os.system("cls || clear")



soma = 0
quantidade = 0
pares = 0
impares = 0
soma_pares = 0
soma_impares = 0

while True:
    num = int(input("Digite um numero: "))

    if num == 0:
        break

    if num % 2 == 0:
        pares += 1
        soma_pares += num

    else:
        impares += 1
        soma_impares += num

    soma += num
    quantidade += 1


if quantidade > 0:

    media = soma / quantidade
    media_pares = soma_pares / pares

    print(f"A soma dos numeros é: {soma}")
    print(f"A media dos numeros é: {media:.2f}")
    print(f"A quantidade de numeros pares é: {pares}")
    print(f"A quantidade de numeros impares é: {impares}")
    print(f"A media dos numeros pares é: {media_pares:.2f}")
else:   
    print ("Valor incorreto! ")


