import os
os.system("cls || clear")




soma = 0


for i in range(3):
   
   while True:

    nota = float(input("Digite a nota: "))

    if nota < 0 and nota > 10:
     
      
     print("Notas validas, digite novamente")

    else:
       
       soma += nota
       break
 
    
media = soma / 3



if media > 7:
   
    resultado = "Aprovado"


elif media >= 5:
   

    resultado = "Recuperação"


else:


 resultado = "Reprovado"



print(f" \nMédia: {media}")
print(f"Resultado: {resultado}")
