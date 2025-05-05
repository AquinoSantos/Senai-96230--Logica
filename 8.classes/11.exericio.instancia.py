import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:

    nome: str
    bibliografia: str

    def exibir_dados(self):

     print(f"Nome: {self.nome}\nBibliografia: {self.bibliografia}\n\n")


   
@dataclass

class Livro:
    titulo: str
    ano: int
    autor: Autor
    

    def exibir_detalhes(self):
     print(f"Título: {self.titulo}\nAno: {self.ano}\nAutor: {self.autor.nome}\n")


lista_livros = []




    
livro = Livro(
                titulo = input("Digite o título do livro: "),
                ano = int(input("Digite o ano do livro: ")),
                autor = Autor(nome = input("Digite o nome do autor: "),
                        bibliografia = input("Digite a bibliografia do autor: "))
                    )
    
lista_livros.append(livro)
    



for livro in lista_livros:
   livro.exibir_detalhes()


nome_arquivo = "Livros.txt"
with open(nome_arquivo, "a") as arquivo_livros:
    arquivo_livros.write(f"Título: {livro.titulo}\nAno: {livro.ano}\nAutor: {livro.autor.nome}\n")






    

