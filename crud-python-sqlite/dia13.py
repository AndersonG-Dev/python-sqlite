import sqlite3
cornn = sqlite3.connect('dia11.db')
cursor = cornn.cursor()

def vender_produto():
    nome_vendido = input("Qual produto foi vendido? ")
    quantidade_vendida = int(input("Quantos intes foram vendidos? "))
        
    cursor.execute ("UPDATE produtos SET quantidade = quantidade -? WHERE nome = ?", (quantidade_vendida,nome_vendido))
    cornn.commit()
    
    if cursor.rowcount == 0:
        print(f"\nError: O produto '{nome_vendido}' não existe. Nenhuma baixa foi feita.")  
    else:    
        print(f"\nSucesso! Baixar de {quantidade_vendida} unidades de '{nome_vendido}' realizada")
vender_produto()