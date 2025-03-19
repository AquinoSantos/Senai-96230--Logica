import os
os.system("cls || clear")



login_teste = "aquino".upper()
senha_teste= "senai".upper()

tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:

    login = input("Digite o login: ").upper()
    senha = input("Digite a senha: ").upper()

    if login == login_teste and senha == senha_teste:

        print("Login realizado com sucesso!")

        break
    else:

        print("Login ou senha incorretos. Tente novamente.")
        tentativas += 1
        

if tentativas == limite_tentativas:

    print("Número máximo de tentativas atingido. Programa encerrado.")


else:
    print()






















