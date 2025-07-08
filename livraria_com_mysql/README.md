# 📚 Projeto Livraria com MySQL

Este é um projeto simples em Python que permite:

- Cadastrar livros via terminal;
- Armazenar os dados em um banco de dados MySQL;
- Exibir os livros cadastrados;
- Buscar um livro pelo título.

## 🚀 Tecnologias usadas

- Python 3.13
- MySQL
- mysql-connector-python

## 💻 Como executar

1. Configure o banco de dados MySQL com uma tabela chamada `livraria`:

```sql
CREATE DATABASE biblioteca;

USE biblioteca;

CREATE TABLE livraria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    autor VARCHAR(100),
    quantidade INT
);
