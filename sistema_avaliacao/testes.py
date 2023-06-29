import unittest
from controllers import TipoQuestaoController, TipoUsuarioController, ProvaController, UsuarioController, QuestaoController, ProvaQuestaoController, ResultadoController

class TestTipoQuestaoController(unittest.TestCase):
    def setUp(self):
        self.controller = TipoQuestaoController()

    def tearDown(self):
        self.controller.excluir_tipo_questao(1)

    def test_criar_tipo_questao(self):
        self.controller.criar_tipo_questao(1, 'Teste')
        tipo_questao = self.controller.recuperar_tipo_questao(1)
        self.assertEqual(tipo_questao['id'], 1)
        self.assertEqual(tipo_questao['nome'], 'Teste')

    def test_atualizar_tipo_questao(self):
        self.controller.criar_tipo_questao(1, 'Teste')
        self.controller.atualizar_tipo_questao(1, 'Novo Teste')
        tipo_questao = self.controller.recuperar_tipo_questao(1)
        self.assertEqual(tipo_questao['nome'], 'Novo Teste')

    def test_excluir_tipo_questao(self):
        self.controller.criar_tipo_questao(1, 'Teste')
        self.controller.excluir_tipo_questao(1)
        tipo_questao = self.controller.recuperar_tipo_questao(1)
        self.assertIsNone(tipo_questao)

class TestUsuarioController(unittest.TestCase):
    def setUp(self):
        self.controller = UsuarioController()

    def tearDown(self):
        self.controller.excluir_usuario(1)

    def test_criar_usuario(self):
        self.controller.criar_usuario(1, 'Otavio', 'otavio@example.com')
        usuario = self.controller.recuperar_usuario(1)
        self.assertEqual(usuario['id'], 1)
        self.assertEqual(usuario['nome'], 'Otavio')
        self.assertEqual(usuario['email'], 'otavio@example.com')

    def test_atualizar_usuario(self):
        self.controller.criar_usuario(1, 'Otavio', 'otavio@example.com')
        self.controller.atualizar_usuario(1, 'Camilo', 'camilo@example.com')
        usuario = self.controller.recuperar_usuario(1)
        self.assertEqual(usuario['nome'], 'Camilo')
        self.assertEqual(usuario['email'], 'camilo@example.com')

    def test_excluir_usuario(self):
        self.controller.criar_usuario(1, 'Otavio', 'otavio@example.com')
        self.controller.excluir_usuario(1)
        usuario = self.controller.recuperar_usuario(1)
        self.assertIsNone(usuario)


class TestProvaController(unittest.TestCase):
    def setUp(self):
        self.controller = ProvaController()

    def tearDown(self):
        self.controller.excluir_prova(1)

    def test_criar_prova(self):
        self.controller.criar_prova(1, '2023-06-29')
        prova = self.controller.recuperar_prova(1)
        self.assertEqual(prova['id_prova'], 1)
        self.assertEqual(prova['data_prova'], '2023-06-29')

    def test_atualizar_prova(self):
        self.controller.criar_prova(1, '2023-06-29')
        self.controller.atualizar_prova(1, '2023-07-01')
        prova = self.controller.recuperar_prova(1)
        self.assertEqual(prova['data_prova'], '2023-07-01')

    def test_excluir_prova(self):
        self.controller.criar_prova(1, '2023-06-29')
        self.controller.excluir_prova(1)
        prova = self.controller.recuperar_prova(1)
        self.assertIsNone(prova)

class TestUsuarioController(unittest.TestCase):
    def setUp(self):
        self.controller = TipoUsuarioController()

    def tearDown(self):
        self.controller.excluir_usuario(1)

    def test_criar_usuario(self):
        self.controller.criar_usuario(1, 'John Doe', 'johndoe@example.com')
        usuario = self.controller.recuperar_usuario(1)
        self.assertEqual(usuario['id'], 1)
        self.assertEqual(usuario['nome'], 'John Doe')
        self.assertEqual(usuario['email'], 'johndoe@example.com')

    def test_atualizar_usuario(self):
        self.controller.criar_usuario(1, 'John Doe', 'johndoe@example.com')
        self.controller.atualizar_usuario(1, 'Jane Doe', 'janedoe@example.com')
        usuario = self.controller.recuperar_usuario(1)
        self.assertEqual(usuario['nome'], 'Jane Doe')
        self.assertEqual(usuario['email'], 'janedoe@example.com')

    def test_excluir_usuario(self):
        self.controller.criar_usuario(1, 'John Doe', 'johndoe@example.com')
        self.controller.excluir_usuario(1)
        usuario = self.controller.recuperar_usuario(1)
        self.assertIsNone(usuario)

class TestQuestaoController(unittest.TestCase):
    def setUp(self):
        self.controller = QuestaoController()

    def tearDown(self):
        self.controller.excluir_questao(1)

    def test_criar_questao(self):
        self.controller.criar_questao(1, 'Qual é a capital do Brasil?', 'Brasília', 'Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Juiz de Fora', 'Brasília', 1, 1)
        questao = self.controller.recuperar_questao(1)
        self.assertEqual(questao['id_questao'], 1)
        self.assertEqual(questao['descricao_questao'], 'Qual é a capital do Brasil?')
        self.assertEqual(questao['questao_correta'], 'Brasília')

    def test_atualizar_questao(self):
        self.controller.criar_questao(1, 'Qual é a capital do Brasil?', 'Brasília', 'Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Juiz de Fora', 'Brasília', 1, 1)
        self.controller.atualizar_questao(1, 'Qual é a capital do Brasil?', 'Brasília', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Juiz de Fora', 'Brasília', 1, 1)
        questao = self.controller.recuperar_questao(1)
        self.assertEqual(questao['alternativa_c'], 'São Paulo')

    def test_excluir_questao(self):
        self.controller.criar_questao(1, 'Qual é a capital do Brasil?', 'Brasília', 'Rio de Janeiro', 'Sao Paulo', 'Belo Horizonte', 'Juiz de Fora', 'Brasília', 1, 1)
        self.controller.excluir_questao(1)
        questao = self.controller.recuperar_questao(1)
        self.assertIsNone(questao)

class TestProvaQuestaoController(unittest.TestCase):
    def setUp(self):
        self.controller = ProvaQuestaoController()

    def tearDown(self):
        self.controller.remover_questao_da_prova(1, 1, 1)

    def test_adicionar_questao_prova(self):
        self.controller.adicionar_questao_na_prova(1, 1, 1)
        prova_questao = self.controller.recuperar_questoes_da_prova(1, 1, 1)
        self.assertIsNotNone(prova_questao)

    def test_remover_questao_prova(self):
        self.controller.adicionar_questao_na_prova(1, 1, 1)
        self.controller.remover_questao_da_prova(1, 1, 1)
        prova_questao = self.controller.recuperar_questoes_da_prova(1, 1, 1)
        self.assertIsNone(prova_questao)

class TestResultadoController(unittest.TestCase):
    def setUp(self):
        self.controller = ResultadoController()

    def tearDown(self):
        self.controller.excluir_resultado(1, 1, 90, 1)

    def test_registrar_resultado(self):
        self.controller.criar_resultado(1, 1, 90, 1)
        resultado = self.controller.recuperar_resultado(1, 1)
        self.assertEqual(resultado['id_prova'], 1)
        self.assertEqual(resultado['id_usuario'], 1)
        self.assertEqual(resultado['pontuacao'], 90)

    def test_atualizar_resultado(self):
        self.controller.criar_resultado(1, 1, 90, 1)
        self.controller.atualizar_resultado(1, 1, 95)
        resultado = self.controller.recuperar_resultado(1, 1)
        self.assertEqual(resultado['pontuacao'], 95)

    def test_excluir_resultado(self):
        self.controller.criar_resultado(1, 1, 90, 1)
        self.controller.excluir_resultado(1, 1)
        resultado = self.controller.recuperar_resultado(1, 1)
        self.assertIsNone(resultado)

if __name__ == '__main__':
    unittest.main()
