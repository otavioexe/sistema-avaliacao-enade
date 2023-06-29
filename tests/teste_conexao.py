import pymysql

def testar_conexao():
    try:
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="7321",
            database="ENADE"
        )
        if conn.open:
            print('Conexão com o banco de dados estabelecida com sucesso!')
    except pymysql.Error as error:
        print(f'Erro ao conectar ao banco de dados: {error}')
    finally:
        conn.close()

testar_conexao()
