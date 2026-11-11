import sqlite3
cornn = sqlite3.connect('dia11.db')
cursor = cornn.cursor()

def buscar_produto():

    nome = input("Digite o nome do produto que deseja buscar: ")
    pesquisa = f"%{nome}%"

    cursor.execute("SELECT * FROM produtos WHERE nome LIKE ?", (pesquisa,))
    resultado = cursor.fetchall()
    
    if len(resultado) == 0:
        print("\n O produto não foi encontrado")
    else:
        for produto in resultado:
            print(f"Nome: {produto[1]} | Preço: R${produto[2]:,.2f} | Quantidade: {produto[3]}")
buscar_produto()