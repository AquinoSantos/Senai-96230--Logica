import os
os.system("cls || clear")


soma = 0
quantidade = 0

while True:
    num = int(input("Digite um numero: "))

    if num < 0:

        break

    

    soma += num
    quantidade += 1

if quantidade > 0 :

    media =soma / quantidade
    print(f"A soma dos numeros digitados é : {soma:}")
    print(f"A media dos numeros é: {media}")

else:
    print("Valor incorreto!")




 
