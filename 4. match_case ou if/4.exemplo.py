import os
os.system("clear")

print("Mes do ano\n")
print("Mensagem do mes\n")
mes = int(input("""
                
Codigo\t Mes\t\t\t\t\t\tMensagem
  1 \tJaneiro\t\t"Janeiro é o 'Janeiro Branco', mês da proteção a saude mental!"
  2 \tFevereiro\t"Fevereiro é o 'Fevereiro Laranja ', mês de conscientização sobre a Leucemia!"
  3 \tMarço\t\t"Março é o 'Março Azul Escuro', mês de conscientização ao cancer de colorretal!"
  4 \tAbril\t\t"Abril é o 'Abril Azul', mês de conscientização sobre o autismo!"
  5 \tMaio\t\t"Maio é o 'Maio Amarelo', mês de prevenção aos acidentes de transito!"
  6 \tJunho \t\t"Junho é o 'Junho Vermelho', mês de conscientização a doação de sangue!"
  7 \tJulho\t\t"Julho é o 'Julho Amarelo', mês conscientização sobre o cancer osseo!" 
  8 \tAgosto\t\t"Agosto é o 'Agosto Dourado', mês da conscientização sobre o aleitamento materno!"
  9 \tSetembro\t"Setembro é o 'Setembro vermelho', mês da conscientização sobre saude do coração!"
  10 \tOutubro\t\t"Outubro é o 'Outubro rosa', mês de conscientização sobre o cancer de mama!"
  11 \tNovembro\t"Novembro é o 'Novembro azul', mês de combate ao cancer de prostata!"
  12 \tDezembro\t"Dezembro é o 'Dezembro laranja', mês de prevenção ao cancer de pele!"  

 Digite um numero de 1 a 12: """))



match mes :

     case 1:
      Mes = "Janeiro"
      Mensagem = "Janeiro é o 'Janeiro Branco', mês da proteção a saude mental!"
     
    
    
     case 2:
          Mes = "Fevereiro"
          Mensagem = "Fevereiro é o 'Fevereiro Laranja ', mês de conscientização sobre a Leucemia!"

     case 3:
        Mes = "Março"
        Mensagem = "Março é o 'Março Azul Escuro', mês de conscientização ao cancer de colorretal!"
      
     case 4:
        Mes = "Abril"
        Mensagem = "Abril é o 'Abril Azul', mês de conscientização sobre o autismo!"
      
     case 5:
        Mes = "Maio"
        Mensagem = "Maio é o 'Maio Amarelo', mês de prevenção aos acidentes de transito!"
      
     case 6:
        Mes = "Junho"
        Mensagem = "Junho é o 'Junho Vermelho', mês de conscientização a doação de sangue!"
      
     case 7:
        Mes = "Julho"
        Mensagem = "Julho é o 'Julho Amarelo', mês conscientização sobre o cancer osseo!"

     case 8:
        Mes = "Agosto"
        Mensagem = "Agosto é o 'Agosto Dourado', mês da conscientização sobre o aleitamento materno!"
      
     case 9:
        Mes = "Setembro"
        Mensagem = "Setembro é o 'Setembro vermelho', mês da conscientização sobre saude do coração!"
      
     case 10:
        Mes = "Outubro"
        Mensagem = "Outubro é o 'Outubro rosa', mês de conscientização sobre o cancer de mama!"
      
     case 11:
        Mes = "Novembro"
        Mensagem = "Novembro é o 'Novembro azul', mês de combate ao cancer de prostata!"

     case 12:
        Mes = "Dezembro"
        Mensagem = "Dezembro é o 'Dezembro laranja', mês de prevenção ao cancer de pele!"
      
     case _: 
        Mes = "Opção invalida"
        Mensagem = "Mensagem invalida"

print(f"\nMes escolhido:  {Mes}")
print(f"Mensagem:  {Mensagem}")
print("===FIM===")
