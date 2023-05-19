import mysql.connector

# Configuração da conexão
mydb = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': '',
    'raise_on_warnings': True
}

connection = mysql.connector.connect(**mydb)
