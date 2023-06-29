from dao import TipoQuestaoDAO, TipoUsuarioDAO, ProvaDAO, UsuarioDAO, QuestaoDAO, ProvaQuestaoDAO, ResultadoDAO

class TipoQuestaoController:
    def __init__(self):
        self.dao = TipoQuestaoDAO()

    def criar_tipo_questao(self, id_tipo_questao, nome_tipo_questao):
        self.dao.criar_tipo_questao(id_tipo_questao, nome_tipo_questao)

    def recuperar_tipo_questao(self, id_tipo_questao):
        return self.dao.recuperar_tipo_questao(id_tipo_questao)

    def atualizar_tipo_questao(self, id_tipo_questao, novo_nome_tipo_questao):
        self.dao.atualizar_tipo_questao(id_tipo_questao, novo_nome_tipo_questao)

    def excluir_tipo_questao(self, id_tipo_questao):
        self.dao.excluir_tipo_questao(id_tipo_questao)

#----------------------------------------------------

class TipoUsuarioController:
    def __init__(self):
        self.dao = TipoUsuarioDAO()

    def criar_tipo_usuario(self, id_tipo_usuario, nome_tipo_usuario):
        self.dao.criar_tipo_usuario(id_tipo_usuario, nome_tipo_usuario)

    def recuperar_tipo_usuario(self, id_tipo_usuario):
        return self.dao.recuperar_tipo_usuario(id_tipo_usuario)

    def atualizar_tipo_usuario(self, id_tipo_usuario, novo_nome_tipo_usuario):
        self.dao.atualizar_tipo_usuario(id_tipo_usuario, novo_nome_tipo_usuario)

    def excluir_tipo_usuario(self, id_tipo_usuario):
        self.dao.excluir_tipo_usuario(id_tipo_usuario)

#----------------------------------------------------

class ProvaController:
    def __init__(self):
        self.dao = ProvaDAO()

    def criar_prova(self, id_prova, data_prova):
        self.dao.criar_prova(id_prova, data_prova)

    def recuperar_prova(self, id_prova):
        return self.dao.recuperar_prova(id_prova)

    def atualizar_prova(self, id_prova, nova_data_prova):
        self.dao.atualizar_prova(id_prova, nova_data_prova)

    def excluir_prova(self, id_prova):
        self.dao.excluir_prova(id_prova)

#----------------------------------------------------

class UsuarioController:
    def __init__(self):
        self.dao = UsuarioDAO()

    def criar_usuario(self, id_usuario, nome, email, senha, id_tipo_usuario):
        self.dao.criar_usuario(id_usuario, nome, email, senha, id_tipo_usuario)

    def recuperar_usuario(self, id_usuario):
        return self.dao.recuperar_usuario(id_usuario)

    def atualizar_usuario(self, id_usuario, novo_nome, novo_email, nova_senha, novo_id_tipo_usuario):
        self.dao.atualizar_usuario(id_usuario, novo_nome, novo_email, nova_senha, novo_id_tipo_usuario)

    def excluir_usuario(self, id_usuario):
        self.dao.excluir_usuario(id_usuario)

#----------------------------------------------------

class QuestaoController:
    def __init__(self):
        self.dao = QuestaoDAO()

    def criar_questao(self, id_questao, descricao_questao, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, questao_correta, estado_questao, id_tipo_questao):
        self.dao.criar_questao(id_questao, descricao_questao, alternativa_a, alternativa_b, alternativa_c, alternativa_d, alternativa_e, questao_correta, estado_questao, id_tipo_questao)

    def recuperar_questao(self, id_questao):
        return self.dao.recuperar_questao(id_questao)

    def atualizar_questao(self, id_questao, nova_descricao_questao, nova_alternativa_a, nova_alternativa_b, nova_alternativa_c, nova_alternativa_d, nova_alternativa_e, nova_questao_correta, novo_estado_questao, novo_id_tipo_questao):
        self.dao.atualizar_questao(id_questao, nova_descricao_questao, nova_alternativa_a, nova_alternativa_b, nova_alternativa_c, nova_alternativa_d, nova_alternativa_e, nova_questao_correta, novo_estado_questao, novo_id_tipo_questao)

    def excluir_questao(self, id_questao):
        self.dao.excluir_questao(id_questao)

#----------------------------------------------------

class ProvaQuestaoController:
    def __init__(self):
        self.dao = ProvaQuestaoDAO()

    def adicionar_questao_na_prova(self, id_prova, id_questao):
        self.dao.adicionar_questao_na_prova(id_prova, id_questao)

    def remover_questao_da_prova(self, id_prova, id_questao):
        self.dao.remover_questao_da_prova(id_prova, id_questao)

    def recuperar_questoes_da_prova(self, id_prova):
        return self.dao.recuperar_questoes_da_prova(id_prova)

    def atualizar_questao_na_prova(self, id_prova, id_questao_antiga, id_questao_nova):
        self.dao.atualizar_questao_na_prova(id_prova, id_questao_antiga, id_questao_nova)

#----------------------------------------------------

class ResultadoController:
    def __init__(self):
        self.dao = ResultadoDAO()

    def criar_resultado(self, id_resultado, valor_obtido, id_usuario, id_prova):
        self.dao.criar_resultado(id_resultado, valor_obtido, id_usuario, id_prova)

    def recuperar_resultado(self, id_resultado):
        return self.dao.recuperar_resultado(id_resultado)

    def atualizar_resultado(self, id_resultado, novo_valor_obtido, novo_id_usuario, novo_id_prova):
        self.dao.atualizar_resultado(id_resultado, novo_valor_obtido, novo_id_usuario, novo_id_prova)

    def excluir_resultado(self, id_resultado):
        self.dao.excluir_resultado(id_resultado)
