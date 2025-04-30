import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Paciente:
    #Atributos: são variaveis que pertencem a classe.
    nome: str
    idade: int


    #Método: é uma função que pertence a classe.
    #Este método para exibir dados do paciente.
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\n\n")


#Atribuindo dados ao paciente1.
paciente1= Paciente(
                 nome= input("Digite seu nome: "),
                 idade= input("Digite seu nome:" ),
                )


#Exibindo dados do paciente
paciente1.exibir_dados()

