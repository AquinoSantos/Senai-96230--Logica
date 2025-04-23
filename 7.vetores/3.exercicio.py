import os
os.system("cls || clear")


lista_numeros = []
QUANTIDADE_NUMEROS = 5
positivos = 0
negativos = 0 
soma_positivos = 0




for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)

    if numero < 0:
        negativos += 1
        
    else:
        positivos += 1
        soma_positivos += numero
    
    

    

print(f"Quantidade de números negativos: {negativos}")
print(f"Quantidade de numeros positivos: {positivos}")
print(f"A soma dos numeros positivos é: {soma_positivos}")
    
    


