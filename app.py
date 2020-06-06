from connection_factory import ConnectionFactory

connection = ConnectionFactory().get_connection()

cursor = connection.cursor()

# cursor.execute("CREATE DATABASE alura")
# cursor.execute("CREATE TABLE cursos (nome VARCHAR(255), descricao VARCHAR(255))")
cursor.execute('SELECT * FROM cursos')

for linha in cursor:
    print(linha)

connection.close()
