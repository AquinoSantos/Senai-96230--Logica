import os
os.system("clear")

# Solicita ao usuário a quantidade de maçãs desejadas
quantidade = int(input("Digite a quantidade de maçãs desejadas: "))

# Define o preço por unidade baseado na quantidade
if quantidade < 12:
    
    preco = 1.30

else:
    preco = 1.00

# Calcula o valor total
valor = quantidade * preco

# Mostra o valor total
print(f"O valor total é: R$ {valor}")