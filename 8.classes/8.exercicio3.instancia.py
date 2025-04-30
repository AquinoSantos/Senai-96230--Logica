import os

from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Paciente:
    #Atributos: são variaveis que pertencem a classe.
    nome: str
    idade: int
    peso: float
    altura: float


    #Método: é uma função que pertence a classe.
    #Este método para exibir dados do paciente.
    def exibir_dados(self):
        print(f"\nNome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}\nAltura: {self.altura}\n\n")


#criando lista
lista_pacientes= []



#Atribuindo dados aos pacientes.
for i in range(4):
    paciente = Paciente( 
                     
                     nome= input(f"\nDigite o nome do {i + 1}º paciente: "),
                     idade= int(input(f"Digite a idade do {i + 1}º paciente: ")),
                     peso= float(input(f"Digite o peso do {i + 1}º paciente: ")),
                     altura= float(input(f"Digite a altura do {i + 1}º paciente: "))
                     )
                    
    
    lista_pacientes.append(paciente)


#Exibindo dados do paciente
for paciente in lista_pacientes:
    paciente.exibir_dados()





















