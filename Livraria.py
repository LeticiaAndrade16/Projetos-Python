'''
🧾 Exercício: Sistema de Estoque de Livros
Crie um sistema simples para gerenciar o estoque de livros de uma livraria.

📚 Requisitos:
Cadastrar Livros

Peça: título, autor e quantidade em estoque.

Continue cadastrando até o usuário digitar "sair".

Armazenar os livros

Cada livro deve ser armazenado como uma estrutura organizada (classe ou dicionário).

Exibir catálogo

Mostre todos os livros cadastrados com: Título | Autor | Quantidade.

Permitir busca por título

O usuário digita o nome de um livro e o sistema mostra os dados dele, se existir.
'''

import mysql.connector

# Conectar ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    port=3306,
    user='root',
    password='81194',
    database='biblioteca'
)

cursor = conexao.cursor()


class Livraria:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

    def info(self, index):
        print(f'{index}. {self.titulo} | {self.autor} | {self.quantidade}')


livros = []

while True:
    titulo = input('Informe o nome do livro ou (sair para finalizar): ').capitalize()
    if titulo.lower() == 'sair':
        break

    autor = input('Informe o nome do autor: ').capitalize()
    qtd = int(input('Informe a quantidade: '))

    livro = Livraria(titulo, autor, qtd)
    livros.append(livro)

    # Inserção no banco de dados
    comando = "INSERT INTO livraria (titulo, autor, quantidade) VALUES (%s, %s, %s)"
    valores = (titulo, autor, qtd)
    cursor.execute(comando, valores)
    conexao.commit()

# Exibir todos os livros cadastrados
print('\n📚 Livros Cadastrados:\n')
for index, livro in enumerate(livros, start=1):
    livro.info(index)

# BUSCAR UM LIVRO
busca = input('\nGostaria de buscar um livro (sim/nao): ').lower()
if busca == 'sim':
    buscar = input('\n🔎 Digite o título do livro que deseja encontrar: ').lower()
    encontrado = False

    for index, livro in enumerate(livros, start=1):
        if livro.titulo.lower() == buscar:
            print('\n✅ Livro encontrado:')
            livro.info(index)
            encontrado = True
            break

    if not encontrado:
        print('\n❌ Livro não encontrado')

# Encerrar
cursor.close()
conexao.close()