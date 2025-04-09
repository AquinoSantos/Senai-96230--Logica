import os
os.system("cls || clear ")


def inflacionar(preco):

    if preco < 100:

        return preco * 1.10 # inflaciona 10% 
     
    else:

        return preco * 1.20 # inflaciona 20%
    
    
    return resultado




def desconto(preco):

 if preco < 100:

    return preco * 0.10 # desinflaciona 10%
    
 else:

    return preco * 0.20 # desinflaciona 20%
    
 return resultado






preco_produto = float(input("Digite o preço do produto: R$ "))



preco_inflacionado = inflacionar(preco_produto)


preco_descontado = desconto(preco_produto)




print(f"O preço inflacionado do produto é: R$ {preco_inflacionado:.2f}")

print(f"O preço descontado do produto é: R$ {preco_descontado:.2f}")


















