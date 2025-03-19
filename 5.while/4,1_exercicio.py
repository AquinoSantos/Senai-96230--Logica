import os
os.system("cls || clear ")


login_teste = "aquino".upper()
senha_teste = "senai".upper()



for i in range(3):

    login = input("Digite o login: ").upper()
    senha = input("Digite a senha: ").upper()

    
    if login == login_teste and senha == senha_teste:

        print("Login bem-sucedido!")
        break

    else:

        print("Login ou senha incorretos.")
        if i == 2:

           print("Numero de tentativas atingidas")



    
            

           
        


    
    