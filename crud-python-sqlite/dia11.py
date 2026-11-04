import sqlite3
import os

conn = sqlite3.connect('dia11.db')
cursor = conn.cursor()
# Criando tabelas
def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        quantidade INTEGER NOT NULL
    )''')

create_table()
with open ('lote_produtos.txt' , 'r' , encoding='utf-8') as texto:
    for linha in texto:
            dados = linha.split(',')
            nome = str(dados[0])
            preco = float(dados[1])
            quantidade = int(dados[2])
            print('Nome: ' , nome)
            print('Quantidade: ' , quantidade)
            print('Preço: ' , preco)
            cursor.execute('''INSERT INTO produtos (nome, preco, quantidade)
            VALUES (?, ?, ?)''', (nome, preco, quantidade))
conn.commit()
def list_products():
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:,.2f} | Quantidade: {produto[3]}")
list_products()