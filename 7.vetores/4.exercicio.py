import os
os.system("cls || clear")


lista_valor = []



for i in range(5):
     
     valor = float(input(f"Digite o {i + 1}º valor: "))
     lista_valor.append(valor)

     if valor < 0:

          lista_valor.remove(valor)
          
          lista_valor.append(0)
          
     else:
          valor = lista_valor


print(f"Os valores listados foram: {(lista_valor)}")



     

     
 

               



