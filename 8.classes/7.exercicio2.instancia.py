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


#criando lista
lista_pacientes= []



#Atribuindo dados aos pacientes.
for i in range(2):
    paciente= Paciente(
                    nome= input("Digite o nome do paciente: "),
                    idade= int(input("Digite a idade do paciente: "))
                    )
    
    lista_pacientes.append(paciente)

#salvando em arquivo .txt
nome_arquivo = "Dados_paciente.py"
with open(nome_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_pacientes:
        arquivo_pacientes.write(f"Nome: {paciente.nome}\nIdade: {paciente.idade}\n")


print(f"Dados salvos com sucesso\n")




#Exibindo dados do paciente
for paciente in lista_pacientes:
    paciente.exibir_dados()
