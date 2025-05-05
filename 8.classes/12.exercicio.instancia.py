import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass

class Empresa:
    nome: str
    data_nascimento: str
    rg: str
    cpf:str



    def exibir_dados(self):
        print(f"Nome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nRG: {self.rg}\nCPF: {self.cpf}\n\n")

    
#criando lista
lista_funcionarios = []

#Atribuindo dados aos funcionarios.
for i in range(5):
    funcionario = Empresa(
                    nome= input(f"Digite o nome do {i + 1}º funcionario: "),
                    data_nascimento= input(f"Digite a data de nascimento do {i + 1}º funcionario: "),
                    rg= input(f"Digite o RG do {i + 1}º funcionario: "),
                    cpf= input(f"Digite o CPF do {i + 1}º funcionario:"),
                    )
    
    lista_funcionarios.append(funcionario)

#salvando em arquivo .txt
nome_arquivo = "Funcionarios_sub.txt"
with open(nome_arquivo, "a", encoding= "utf-8") as arquivo_funcionarios:
    for funcionario in lista_funcionarios:
        arquivo_funcionarios.write(f"Nome: {funcionario.nome}\nData de Nascimento: {funcionario.data_nascimento}\nRG: {funcionario.rg}\nCPF: {funcionario.cpf}\n")

print(f"\nDados salvos com sucesso\n")

print("===Lendo dados do arquivo===")


try:
    with open(nome_arquivo, "r", encoding= "utf-8") as arquivo:

        linhas = arquivo.readlines()
        print("Conteúdo do arquivo:")
        
    for linha in linhas:
        print(linha.strip())

except FileNotFoundError:
    print(f"Arquivo não encontrado.")
    





try:
    with open(nome_arquivo, "r") as arquivo_funcionarios:
        conteudo = arquivo_funcionarios.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:

    print(f"Arquivo {nome_arquivo} não encontrado.")