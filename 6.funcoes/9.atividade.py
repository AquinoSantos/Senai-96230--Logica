import os
os.system("cls || clear ")
while True:
        
        nota_um = float(input("Digite a primeira nota do aluno: "))
        nota_dois= float(input("Digite a segunda nota do aluno: "))
        nota_tres = float(input("Digite a terceira nota do aluno: "))


        def resultado(media):

            if media >= 7:

                return "Aprovado"
            
            elif media < 7 and media >= 4:

                return "Em recuperação"
            
            else:

                return "Reprovado"
            
            return resultado

        media_aluno = (nota_um + nota_dois + nota_tres) / 3

        print(f"A média do aluno é: {media_aluno:.0f}")
        print(f"O aluno está: {resultado(media_aluno)}")


        break
        



        

        
 



   
    
 










