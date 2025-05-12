import os
from dataclasses import dataclass

os.system("cls || clear")


@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str
    estado: str


@dataclass
class Aluno:
    nome: str
    data_nascimento: str
    matricula: str
    curso: str
    endereco: Endereco

    def exibir_dados(self):

        print(f"\nNome: {self.nome}\nData de Nascimento: {self.data_nascimento}\nMatricula: {self.matricula}\nCurso: {self.curso}")
        print(f"Endereço: {self.endereco.logradouro}, Nº {self.endereco.numero}, {self.endereco.cidade} - {self.endereco.estado}")


lista_Aluno = []


def menu_Aluno():
    while True:
        print("\n - Menu Alunos - ")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Alunos")
        print("4. Excluir Alunos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno(lista_Aluno)
        elif opcao == "2":
            listar_aluno(lista_Aluno)
        elif opcao == "3":
            atualizar_aluno(lista_Aluno)
        elif opcao == "4":
            excluir_aluno(lista_Aluno)
        elif opcao == "5":
            break
        else:
            print("Opção inválida, tente novamente.")


def verificar_lista_vazia(lista_aluno):
    if not lista_aluno:
        print("\nA lista está vazia.")
        return True
    return False


def adicionar_aluno(lista_Aluno):
    nome = input("Digite o nome do aluno: ")
    data_nascimento = input("Digite a data de nascimento: ")
    matricula = input("Digite sua matrícula: ")
    curso = input("Digite o curso: ")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")

    endereco = Endereco(logradouro, numero, cidade, estado)
    aluno = Aluno(nome, data_nascimento, matricula, curso, endereco)

    lista_Aluno.append(aluno) 
    print(f"\n{nome} adicionado com sucesso.")


def listar_aluno(lista_Aluno):
    if verificar_lista_vazia(lista_Aluno):
        return

    print("\n - Lista de Alunos - ")
    for aluno in lista_Aluno:
        aluno.exibir_dados()


def atualizar_aluno(lista_Aluno):
    if verificar_lista_vazia(lista_Aluno):
        return

    listar_aluno(lista_Aluno)
    
    nome_antigo = input("Digite o nome do aluno que deseja atualizar: ")

    for aluno in lista_Aluno:
        if aluno.nome == nome_antigo:
            novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
            aluno.nome = novo_nome
            print(f"{nome_antigo} foi atualizado para {novo_nome}.")
            return
        
    print(f"\nO aluno {nome_antigo} não foi encontrado.")


def excluir_aluno(lista_Aluno):
    if verificar_lista_vazia(lista_Aluno):
        return

    listar_aluno(lista_Aluno)
    nome_remover = input("Digite o nome do aluno que deseja remover: ")
    for aluno in lista_Aluno:
        if aluno.nome == nome_remover:
            lista_Aluno.remove(aluno)
            print(f"{nome_remover} foi removido com sucesso.")
            return
        
    print(f"O aluno {nome_remover} não foi encontrado.")


menu_Aluno()