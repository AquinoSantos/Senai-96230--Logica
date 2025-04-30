import os

from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Biblioteca:
    #Atributos: são variaveis que pertencem a classe.
    nome: str
    autor: str
    categoria: str
    preço: float


    #Método: é uma função que pertence a classe.
    #Este método para exibir dados do lista.
    def exibir_dados(self):
        print(f"Nome: {self.nome}\nAutor: {self.autor}\nCategoria: {self.categoria}\nPreço: {self.preço}\n\n")


#criando lista
lista_livros= []



#Atribuindo dados aos listas.
for i in range(3):
    livro= Biblioteca(
                    nome= input("Digite o nome do livro: "),
                    autor=  input("Digite a Autor do livro: "),
                    categoria= input("Digite a Categoria do livro: "),
                    preço= float(input("Digite o preço do livro: ")),


                    )
    
    lista_livros.append(livro)

#salvando em arquivo .txt
nome_arquivo = "Catalogo_livros.txt"
with open(nome_arquivo, "a") as Catalogo_livros:
    for livro in lista_livros:
        Catalogo_livros.write(f"\nNome: {livro.nome}\nAutor: {livro.autor}\nCategoria: {livro.categoria}\nPreço: {livro.preço}\n")
        


print(f"\nDados salvos com sucesso\n")




#Exibindo dados do lista
for livro in lista_livros:
    livro.exibir_dados()


