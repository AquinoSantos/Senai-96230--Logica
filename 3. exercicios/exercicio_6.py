import os
os.system("clear")


login = "Aquino"
senha = "123456"

Usuario = input("Digite o nome de Usuario: ")
Senha = input("Digite a senha: ")


if Usuario == login and Senha == senha:
    print("Acesso permitido")
else:
    print("Acesso negado")

print("==FIM==")