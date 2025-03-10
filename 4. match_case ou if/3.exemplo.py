import os
os.system("clear")

print("Dia da semana\n")
print("Mensagem do dia\n")

diadasemana = int(input("""
Codigo\t    Semana\t\t\tMensagem
  1 \t    Domingo\t\t   "Dia de descansar!"
  2 \t Segunda-feira\t\t"Um bom inicio de semana!"
  3 \t  Terça-feira\t     "Preguiça? Que nada, bora trabalhar!"
  4      Quarta-feira\t      "Já estamos no meio da semana!"
  5 \t Quinta-feira\t       "Animo amanha é sexta-feira!"
  6 \t  Sexta-feira\t\t       "SextouuuU!"
  7 \t    Sábado\t\t"Dia de curtir para alguns!"                        

Digite um numero de 1 a 7: """))

match diadasemana:
    case 1:
       Semana = "Domingo"
       Mensagem = "Dia de descansar!"

    case 2:
       Semana = "Segunda-feira"
       Mensagem = "Um bom inicio de semana!"

    case 3:
         Semana = "Terça-feira"
         Mensagem = "Preguiça? Que nada, bora trabalhar!"

    case 4:
         Semana = "Quarta-feira"
         Mensagem = "Já estamos no meio da semana!"

    case 5:
         Semana = "Quinta-feira"
         Mensagem = "Animo amanha é sexta-feira!"

    case 6:
         Semana = "Sexta-feira"
         Mensagem = "SextouuuU!"

    case 7:
         Semana = "Sábado"
         Mensagem = "Dia de curtir para alguns!"

    case _:
         Semana = "Opção invalida!"
         Mensagem = "Mensagem invalida!"


print(f"\nDia da semana:  {Semana}")
print(f"Mensagem:  {Mensagem}")

print("===FIM===")

