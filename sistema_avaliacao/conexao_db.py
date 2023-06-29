from credenciais_db import credencial

def conectar_ao_banco():
    import pymysql
    conn = pymysql.connect(
        host=credencial["host"],
        user=credencial["user"],
        password=credencial["password"],
        database=credencial["db_name"]
    )
    return conn