import os
from dataclasses import dataclass
os.system("cls || clear")



@dataclass
class Funcionario:
    nome_funcionario: str
    data_admissao: str
    matricula: str
    endereco_funcionario: str


def exibir_dados(self):
       print(f"Nome: {self.nome}\nData de Admissão: {self.data_admissao}\nMatricula: {self.matricula}\nEndereço do Funcionario: {self.endereço_funcionario}\n\n")



@dataclass
class Cliente:
    nome_cliente: str
    data_nascimento: str
    endereco_cliente: str


def exibir_dados(self):
        print(f"Nome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nEndereço do Cliente: {self.endereco_cliente}\n")

    


lista_funcionario = []
lista_cliente = []

#Atribuindo dados aos funcionarios.
for i in range(3):   
     funcionario = Funcionario(
                     nome_funcionario = input(f"\nDigite o nome do {i + 1}º funcionario: "),
                     data_admissao= input(f"Digite a data de admissão do {i + 1}º funcionario: "),
                     matricula= input(f"Digite a matricula do {i + 1}º funcionario: "),
                     endereco_funcionario = input(f"Digite o endereço do {i + 1}º funcionario:"),
                     )
     
   
     cliente = Cliente(
                     nome_cliente = input(f"\nDigite o nome do {i + 1}º cliente: "),
                     data_nascimento= input(f"Digite a data de nascimento do {i + 1}º cliente: "),
                     endereco_cliente = input(f"Digite o endereço do {i + 1}º cliente:"),
                     )
     
     lista_funcionario.append(funcionario)
     lista_cliente.append(cliente)
 



nome_arquivo = "Funcionarios_Clientes.txt"
with open(nome_arquivo, "a", encoding= "utf-8") as arquivo_funcionarios:

    for funcionario in lista_funcionario:
        arquivo_funcionarios.write(f"\nNome do Funcionario: {funcionario.nome_funcionario}\nData de Admissão: {funcionario.data_admissao}\nMatricula: {funcionario.matricula}\nEndereço do Funcionario: {funcionario.endereco_funcionario}\n")

    for cliente in lista_cliente:
        arquivo_funcionarios.write(f"\nNome do Cliente: {cliente.nome_cliente}\nData de Nascimento: {cliente.data_nascimento}\nEndereço do Cliente: {cliente.endereco_cliente}\n")        
     
print(f"\nDados salvos com sucesso\n")

print("===Lendo dados do arquivo===\n")

try:
    with open(nome_arquivo, "r", encoding= "utf-8") as arquivo:
        linhas = arquivo.readlines()
        print("Conteúdo do arquivo:")
        
    for linha in linhas:
        print(linha.strip())

except FileNotFoundErrors:
    print(f"Arquivo não encontrado.")


    