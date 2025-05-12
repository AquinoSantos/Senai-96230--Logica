import os
from dataclasses import dataclass

os.system("cls || clear")



@dataclass
class Funcionario:

    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nCPF: {self.cpf}\nFunção: {self.funcao}\n")


funcionarios = []


def menu_funcionario():

    while True:
        print("\n - Menu Funcionário - ")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_funcionario(funcionarios)
        elif opcao == "2":
            listar_funcionarios(funcionarios)
        elif opcao == "3":
            atualizar_funcionario(funcionarios)
        elif opcao == "4":
            excluir_funcionario(funcionarios)
        elif opcao == "5":
            break
        else:
            print("Opção inválida, tente novamente.")

    

def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("\nA lista está vazia.")
        return True
    return False





def adicionar_funcionario(lista_funcionarios):

    nome = input("Digite o nome do funcionário: ")
    data_nascimento = input("Digite a data de nascimento: ")
    cpf = input("Digite o CPF: ")
    funcao = input("Digite a função: ")

    funcionario = Funcionario(nome, data_nascimento, cpf, funcao)

    lista_funcionarios.append(funcionario)
    print(f"\n{nome} adicionado com sucesso.")


def listar_funcionarios(lista_funcionarios):

    if verificar_lista_vazia(lista_funcionarios):
        return

    print("\n - Lista de Funcionários - ")

    for funcionario in lista_funcionarios:
        funcionario.exibir_dados()


def atualizar_funcionario(lista_funcionarios):

    if verificar_lista_vazia(lista_funcionarios):
        return

    listar_funcionarios(lista_funcionarios)
    
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ")

    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_antigo:
            novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
            funcionario.nome = novo_nome
            print(f"{nome_antigo} foi atualizado para {novo_nome}.")
            return
        
    print(f"\nO funcionário {nome_antigo} não foi encontrado.")


def excluir_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return

    listar_funcionarios(lista_funcionarios)
    nome_remover = input("Digite o nome do funcionário que deseja remover: ")
    for funcionario in lista_funcionarios:
        if funcionario.nome == nome_remover:
            lista_funcionarios.remove(funcionario)
            print(f"{nome_remover} foi removido com sucesso.")
            return
        
    print(f"O funcionário {nome_remover} não foi encontrado.")

    
menu_funcionario()

