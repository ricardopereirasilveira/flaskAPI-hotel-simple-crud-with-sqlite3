import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

criar_tabela = "CREATE TABLE IF NOT EXISTS hoteis ( hotel_id TEXT PRIMARY KEY, " \
               "nome VARCHAR(255), estrelas REAL, diaria REAL, cidade VARCHAR(100))"

criar_hotel = "INSERT INTO hoteis (hotel_id, nome, estrelas, diaria, cidade) VALUES ('alpha', 'Alpha Hotel', " \
              "4.3, 321.33, 'Rio de Janeiro')"

cursor.execute(criar_tabela)
cursor.execute(criar_hotel)

conn.commit()
conn.close()