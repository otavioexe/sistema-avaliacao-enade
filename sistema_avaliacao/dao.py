
from conexao_db import conectar_ao_banco
import pymysql

conectar_ao_banco = conectar_ao_banco

class TipoQuestaoDAO:
    def __init__(self):
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def criar_tipo_questao(self, id_tipo_questao, nome_tipo_questao):
        try:
            #Comando SQL para inserir um novo tipo de questão
            sql = "INSERT INTO TipoQuestao (idTipoQuestao, nomeTipoQuestao) VALUES (%s, %s)"
            values = (id_tipo_questao, nome_tipo_questao)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Tipo de questão criado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao criar tipo de questão: {error}")

    def recuperar_tipo_questao(self, id_tipo_questao):
        try:
            #Comando SQL para recuperar um tipo de questão
            sql = "SELECT * FROM TipoQuestao WHERE idTipoQuestao = %s"
            values = (id_tipo_questao,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                tipo_questao = {
                    "idTipoQuestao": result[0],
                    "nomeTipoQuestao": result[1]
                }
                return tipo_questao
            else:
                print("Tipo de questão não encontrado")
        except pymysql.Error as error:
            print(f"Erro ao recuperar tipo de questão: {error}")

    def atualizar_tipo_questao(self, id_tipo_questao, novo_nome_tipo_questao):
        try:
            #Comando SQL para atualizar o nome de um tipo de questão
            sql = "UPDATE TipoQuestao SET nomeTipoQuestao = %s WHERE idTipoQuestao = %s"
            values = (novo_nome_tipo_questao, id_tipo_questao)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Tipo de questão atualizado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar tipo de questão: {error}")

    def excluir_tipo_questao(self, id_tipo_questao):
        try:
            #Comando SQL para excluir um tipo de questão
            sql = "DELETE FROM TipoQuestao WHERE idTipoQuestao = %s"
            values = (id_tipo_questao,)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Tipo de questão excluído com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao excluir tipo de questão: {error}")

    def fechar_conexao(self):
        # Fechando a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()


#-------------------------------------------------------------------------


class TipoUsuarioDAO:
    def __init__(self):
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def criar_tipo_usuario(self, id_tipo_usuario, nome_tipo_usuario):
        try:
            #Comando SQL para inserir um novo tipo de usuário
            sql = "INSERT INTO TipoUsuario (idTipoUsuario, nomeTipoUsuario) VALUES (%s, %s)"
            values = (id_tipo_usuario, nome_tipo_usuario)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Tipo de usuário criado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao criar tipo de usuário: {error}")

    def recuperar_tipo_usuario(self, id_tipo_usuario):
        try:
            #Comando SQL para recuperar um tipo de usuário
            sql = "SELECT * FROM TipoUsuario WHERE idTipoUsuario = %s"
            values = (id_tipo_usuario,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                tipo_usuario = {
                    "idTipoUsuario": result[0],
                    "nomeTipoUsuario": result[1]
                }
                return tipo_usuario
            else:
                print("Tipo de usuário não encontrado")
        except pymysql.Error as error:
            print(f"Erro ao recuperar tipo de usuário: {error}")

    def atualizar_tipo_usuario(self, id_tipo_usuario, novo_nome_tipo_usuario):
        try:
            #Comando SQL para atualizar o nome de um tipo de usuário
            sql = "UPDATE TipoUsuario SET nomeTipoUsuario = %s WHERE idTipoUsuario = %s"
            values = (novo_nome_tipo_usuario, id_tipo_usuario)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Tipo de usuário atualizado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar tipo de usuário: {error}")

    def excluir_tipo_usuario(self, id_tipo_usuario):
        try:
            #Comando SQL para excluir um tipo de usuário
            sql = "DELETE FROM TipoUsuario WHERE idTipoUsuario = %s"
            values = (id_tipo_usuario,)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Tipo de usuário excluído com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao excluir tipo de usuário: {error}")

    def fechar_conexao(self):
        #Fechando a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()


#-------------------------------------------------------------------------


class ProvaDAO:
    def __init__(self):
        #Conectando com o banco de dados
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def criar_prova(self, id_prova, data_prova):
        try:
            #Comando SQL para inserir uma nova prova
            sql = "INSERT INTO Prova (idProva, dataProva) VALUES (%s, %s)"
            values = (id_prova, data_prova)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Prova criada com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao criar prova: {error}")

    def recuperar_prova(self, id_prova):
        try:
            #Comando SQL para recuperar uma prova
            sql = "SELECT * FROM Prova WHERE idProva = %s"
            values = (id_prova,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                prova = {
                    "idProva": result[0],
                    "dataProva": result[1]
                }
                return prova
            else:
                print("Prova não encontrada")
        except pymysql.Error as error:
            print(f"Erro ao recuperar prova: {error}")

    def atualizar_prova(self, id_prova, nova_data_prova):
        try:
            #Comando SQL para atualizar a data de uma prova
            sql = "UPDATE Prova SET dataProva = %s WHERE idProva = %s"
            values = (nova_data_prova, id_prova)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Prova atualizada com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar prova: {error}")

    def excluir_prova(self, id_prova):
        try:
            #Comando SQL para excluir uma prova
            sql = "DELETE FROM Prova WHERE idProva = %s"
            values = (id_prova,)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Prova excluída com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao excluir prova: {error}")

    def fechar_conexao(self):
        # Fechando a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()


#-------------------------------------------------------------------------


class UsuarioDAO:
    def __init__(self):
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def criar_usuario(self, id_usuario, nome, email, senha, tipo_usuario_id):
        try:
            #Comando SQL para inserir um novo usuário
            sql = "INSERT INTO Usuario (idUsuario, nome, email, senha, TipoUsuario_idTipoUsuario) VALUES (%s, %s, %s, %s, %s)"
            values = (id_usuario, nome, email, senha, tipo_usuario_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Usuário criado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao criar usuário: {error}")

    def recuperar_usuario(self, id_usuario):
        try:
            #Comando SQL para recuperar um usuário
            sql = "SELECT * FROM Usuario WHERE idUsuario = %s"
            values = (id_usuario,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                usuario = {
                    "idUsuario": result[0],
                    "nome": result[1],
                    "email": result[2],
                    "senha": result[3],
                    "TipoUsuario_idTipoUsuario": result[4]
                }
                return usuario
            else:
                print("Usuário não encontrado")
        except pymysql.Error as error:
            print(f"Erro ao recuperar usuário: {error}")

    def atualizar_usuario(self, id_usuario, novo_nome, novo_email, nova_senha, novo_tipo_usuario_id):
        try:
            #Comando SQL para atualizar os dados de um usuário
            sql = "UPDATE Usuario SET nome = %s, email = %s, senha = %s, TipoUsuario_idTipoUsuario = %s WHERE idUsuario = %s"
            values = (novo_nome, novo_email, nova_senha, novo_tipo_usuario_id, id_usuario)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Usuário atualizado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar usuário: {error}")

    def excluir_usuario(self, id_usuario):
        try:
            #Comando SQL para excluir um usuário
            sql = "DELETE FROM Usuario WHERE idUsuario = %s"
            values = (id_usuario,)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Usuário excluído com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao excluir usuário: {error}")

    def fechar_conexao(self):
        #Fechando a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()


#-------------------------------------------------------------------------


class QuestaoDAO:
    def __init__(self):
        #Conexão com o banco de dados
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def criar_questao(self, id_questao, descricao, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, questao_correta, estado_questao, tipo_questao_id):
        try:
            #Comando SQL para inserir uma nova questão
            sql = "INSERT INTO Questao (idQuestao, descricaoQuestao, alternativaA, alternativaB, alternativaC, alternativaD, alternativaE, questaoCorreta, estadoQuestao, TipoQuestao_idTipoQuestao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (id_questao, descricao, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, questao_correta, estado_questao, tipo_questao_id)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Questão criada com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao criar questão: {error}")

    def recuperar_questao(self, id_questao):
        try:
            #Comando SQL para recuperar uma questão
            sql = "SELECT * FROM Questao WHERE idQuestao = %s"
            values = (id_questao,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                questao = {
                    "idQuestao": result[0],
                    "descricaoQuestao": result[1],
                    "alternativaA": result[2],
                    "alternativaB": result[3],
                    "alternativaC": result[4],
                    "alternativaD": result[5],
                    "alternativaE": result[6],
                    "questaoCorreta": result[7],
                    "estadoQuestao": result[8],
                    "TipoQuestao_idTipoQuestao": result[9]
                }
                return questao
            else:
                print("Questão não encontrada")
        except pymysql.Error as error:
            print(f"Erro ao recuperar questão: {error}")

    def atualizar_questao(self, id_questao, nova_descricao, nova_alternativa_a, nova_alternativa_b, nova_alternativa_c, nova_alternativa_d, nova_alternativa_e, nova_questao_correta, novo_estado_questao, novo_tipo_questao_id):
        try:
            #Comando SQL para atualizar os dados de uma questão
            sql = "UPDATE Questao SET descricaoQuestao = %s, alternativaA = %s, alternativaB = %s, alternativaC = %s, alternativaD = %s, alternativaE = %s, questaoCorreta = %s, estadoQuestao = %s, TipoQuestao_idTipoQuestao = %s WHERE idQuestao = %s"
            values = (nova_descricao, nova_alternativa_a, nova_alternativa_b, nova_alternativa_c, nova_alternativa_d, nova_alternativa_e, nova_questao_correta, novo_estado_questao, novo_tipo_questao_id, id_questao)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Questão atualizada com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar questão: {error}")

    def excluir_questao(self, id_questao):
        try:
            #Comando SQL para excluir uma questão
            sql = "DELETE FROM Questao WHERE idQuestao = %s"
            values = (id_questao,)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Questão excluída com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao excluir questão: {error}")

    def fechar_conexao(self):
        # Fechando a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()


#-------------------------------------------------------------------------


class ProvaQuestaoDAO:
    def __init__(self):
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def adicionar_questao_na_prova(self, id_prova, id_questao):
        try:
            #Comando SQL para adicionar uma questão em uma prova
            sql = "INSERT INTO Prova_has_Questao (Prova_idProva, Questao_idQuestao) VALUES (%s, %s)"
            values = (id_prova, id_questao)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Questão adicionada à prova com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao adicionar questão à prova: {error}")

    def remover_questao_da_prova(self, id_prova, id_questao):
        try:
            #Comando SQL para remover uma questão de uma prova
            sql = "DELETE FROM Prova_has_Questao WHERE Prova_idProva = %s AND Questao_idQuestao = %s"
            values = (id_prova, id_questao)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Questão removida da prova com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao remover questão da prova: {error}")

    def recuperar_questoes_da_prova(self, id_prova):
        try:
            #Comando SQL para recuperar as questões de uma prova
            sql = "SELECT * FROM Prova_has_Questao WHERE Prova_idProva = %s"
            values = (id_prova,)
            self.cursor.execute(sql, values)
            results = self.cursor.fetchall()
            if results:
                questoes = [result[0] for result in results]
                return questoes
            else:
                print("Nenhuma questão encontrada para a prova")
        except pymysql.Error as error:
            print(f"Erro ao recuperar questões da prova: {error}")

    def atualizar_questao_na_prova(self, id_prova, id_questao_antiga, id_questao_nova):
        try:
            #Comando SQL para atualizar uma questão em uma prova
            sql = "UPDATE Prova_has_Questao SET Questao_idQuestao = %s WHERE Prova_idProva = %s AND Questao_idQuestao = %s"
            values = (id_questao_nova, id_prova, id_questao_antiga)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Questão atualizada na prova com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar questão na prova: {error}")

    def fechar_conexao(self):
        # Fechandoo a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()



#-------------------------------------------------------------------------


class ResultadoDAO:
    def __init__(self):
        self.conn = conectar_ao_banco()
        self.cursor = self.conn.cursor()

    def criar_resultado(self, id_resultado, valor_obtido, id_usuario, id_prova):
        try:
            #Comando SQL para criar um novo resultado
            sql = "INSERT INTO Resultado (idResultado, valorObtido, Usuario_idUsuario, Prova_idProva) VALUES (%s, %s, %s, %s)"
            values = (id_resultado, valor_obtido, id_usuario, id_prova)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Resultado criado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao criar resultado: {error}")

    def recuperar_resultado(self, id_resultado):
        try:
            #Comando SQL para recuperar um resultado
            sql = "SELECT * FROM Resultado WHERE idResultado = %s"
            values = (id_resultado,)
            self.cursor.execute(sql, values)
            result = self.cursor.fetchone()
            if result:
                resultado = {
                    "idResultado": result[0],
                    "valorObtido": result[1],
                    "Usuario_idUsuario": result[2],
                    "Prova_idProva": result[3]
                }
                return resultado
            else:
                print("Resultado não encontrado")
        except pymysql.Error as error:
            print(f"Erro ao recuperar resultado: {error}")

    def atualizar_resultado(self, id_resultado, novo_valor_obtido):
        try:
            #Comando SQL para atualizar o valor obtido de um resultado
            sql = "UPDATE Resultado SET valorObtido = %s WHERE idResultado = %s"
            values = (novo_valor_obtido, id_resultado)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Resultado atualizado com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao atualizar resultado: {error}")

    def excluir_resultado(self, id_resultado):
        try:
            #Comando SQL para excluir um resultado
            sql = "DELETE FROM Resultado WHERE idResultado = %s"
            values = (id_resultado,)
            self.cursor.execute(sql, values)
            self.conn.commit()
            print("Resultado excluído com sucesso!")
        except pymysql.Error as error:
            print(f"Erro ao excluir resultado: {error}")

    def fechar_conexao(self):
        # Fechando a conexão com o banco de dados
        self.cursor.close()
        self.conn.close()
