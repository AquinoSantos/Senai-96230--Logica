import os
os.system("cls || clear")



def imc_calculo(peso, altura, nome):

    imc = peso / (altura * 2)

    if imc < 18.5:

        classificacao = "Abaixo do peso"

        recomendacao = "Consulte um nutricionista para orientação."

    elif 18.5 <= imc < 24.9:
        classificacao = "Peso normal"
        recomendacao = "Mantenha hábitos saudáveis!"

    elif  imc  >= 25 and < 29.9:
        classificacao = "Sobrepeso"
        recomendacao = "Considere um dieta balanceada e atividade fisica."

    elif imc >= 30 or imc < 34.9:
        classificacao = "Obesidade grau 1"
        recomendacao = "Procure orientação de um profissional de saude."
    
    return f"{nome}, seu IMC é: {imc:.2f}\nClassificação: {classificacao}\nRecomendação: {recomendacao}"





  


