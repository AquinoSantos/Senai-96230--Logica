import os
os.system("cls || clear")




QUANTIDADE_NUMEROS = 5


def solicitar_dados():
     
    lista_numeros = []

    for i in range(QUANTIDADE_NUMEROS):

        numero = int(input(f"Digite o {i + 1}º número: "))
        lista_numeros.append(numero)
    return lista_numeros

def verificar_positivos_negativos(lista):

    negativos = 0
    positivos = 0
    soma_positivos = 0

    for numero in lista:
        if numero < 0:
            negativos += 1
        else:
            positivos += 1
            soma_positivos += numero

    return negativos, positivos, soma_positivos


    print(f"Quantidade de números negativos: {negativos}")
    print(f"Quantidade de numeros positivos: {positivos}")
    print(f"A soma dos numeros positivos é: {soma_positivos}")
   
    

