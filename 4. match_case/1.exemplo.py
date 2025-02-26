import os
os.system("clear")

# Faça um algoritmo que solicite ao usuario dois numeros
#e um carctere que calcula as operaçoes basicas( + - * /).
# Mostre os numeros informados pelo usuario,
# o operador escolhido e o resultado.

#entrada
numero_um = int(input("Digite o primeiro numero: "))
operador = input("Digite a operação que deseja (+ - * /): ")
numero_dois = int(input("Digite um numero: "))

#processamento
match operador:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        resultado = "Opção invalida"

#saida
print(f"\nPrimeiro numero:  {numero_um}")
print(f"Operação:  {operador}")
print(f"Segundo numero:  {numero_dois}")
print(f"Resultado:  {resultado}")
