import unittest
import requests
import time


class TestTipoQuestaoAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_criar_tipo_questao(self):
        url = self.base_url + '/tipoquestao'
        dados = {'id': 1, 'nome': 'Múltipla Escolha'}
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Tipo de questão criado com sucesso'})

    def test_atualizar_tipo_questao(self):
        url = self.base_url + '/tipoquestao/1'
        dados = {'nome': 'Verdadeiro/Falso'}
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Tipo de questão atualizado com sucesso'})

    def test_excluir_tipo_questao(self):
        url = self.base_url + '/tipoquestao/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Tipo de questão excluído com sucesso'})


class TestTipoUsuarioAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_criar_tipo_usuario(self):
        url = self.base_url + '/tipousuario'
        dados = {'id': 1, 'nome': 'Aluno'}
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Tipo de usuário criado com sucesso'})

    def test_atualizar_tipo_usuario(self):
        url = self.base_url + '/tipousuario/1'
        dados = {'nome': 'Professor'}
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Tipo de usuário atualizado com sucesso'})

    def test_excluir_tipo_usuario(self):
        url = self.base_url + '/tipousuario/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Tipo de usuário excluído com sucesso'})


class TestProvaAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_criar_prova(self):
        url = self.base_url + '/prova'
        dados = {'id': 1, 'data': '2023-06-30'}
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Prova criada com sucesso'})

    def test_atualizar_prova(self):
        url = self.base_url + '/prova/1'
        dados = {'data': '2023-07-01'}
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Prova atualizada com sucesso'})

    def test_excluir_prova(self):
        url = self.base_url + '/prova/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Prova excluída com sucesso'})


class TestUsuarioAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_criar_usuario(self):
        url = self.base_url + '/usuario'
        dados = {'id': 1, 'nome': 'João', 'email': 'joao@example.com', 'senha': '123456', 'id_tipo_usuario': 1}
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Usuário criado com sucesso'})

    def test_atualizar_usuario(self):
        url = self.base_url + '/usuario/1'
        dados = {'nome': 'Maria', 'email': 'maria@example.com', 'senha': '654321', 'id_tipo_usuario': 2}
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Usuário atualizado com sucesso'})

    def test_excluir_usuario(self):
        url = self.base_url + '/usuario/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Usuário excluído com sucesso'})


class TestQuestaoAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_criar_questao(self):
        url = self.base_url + '/questao'
        dados = {
            'id': 1,
            'descricao': 'Qual é a capital do Brasil?',
            'alternativaA': 'São Paulo',
            'alternativaB': 'Rio de Janeiro',
            'alternativaC': 'Brasília',
            'alternativaD': 'Salvador',
            'alternativaE': 'Porto Alegre',
            'questaoCorreta': 'C',
            'estado': 'Ativa',
            'id_tipo_questao': 1
        }
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Questão criada com sucesso'})

    def test_atualizar_questao(self):
        url = self.base_url + '/questao/1'
        dados = {
            'descricao': 'Qual é a capital da Argentina?',
            'alternativaA': 'Buenos Aires',
            'alternativaB': 'São Paulo',
            'alternativaC': 'Rio de Janeiro',
            'alternativaD': 'Brasília',
            'alternativaE': 'Montevidéu',
            'questaoCorreta': 'A',
            'estado': 'Inativa',
            'id_tipo_questao': 2
        }
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Questão atualizada com sucesso'})

    def test_excluir_questao(self):
        url = self.base_url + '/questao/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Questão excluída com sucesso'})


class TestProvaQuestaoAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_adicionar_questao_prova(self):
        url = self.base_url + '/provaquestao'
        dados = {'id_prova': 1, 'id_questao': 1}
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Questão adicionada à prova com sucesso'})

    def test_remover_questao_prova(self):
        url = self.base_url + '/provaquestao/1/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Questão removida da prova com sucesso'})

    def test_atualizar_questao_prova(self):
        url = self.base_url + '/provaquestao/1/1'
        dados = {'nova_questao': 2}
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Questão atualizada na prova com sucesso'})

class TestResultadoAPI(unittest.TestCase):
    base_url = 'http://localhost:5000'

    def test_criar_resultado(self):
        url = self.base_url + '/resultado'
        dados = {'id': 1, 'id_prova': 1, 'id_usuario': 1, 'nota': 8.5}
        response = requests.post(url, json=dados)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {'mensagem': 'Resultado criado com sucesso'})

    def test_atualizar_resultado(self):
        url = self.base_url + '/resultado/1'
        dados = {'nota': 9.0}
        response = requests.put(url, json=dados)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Resultado atualizado com sucesso'})

    def test_excluir_resultado(self):
        url = self.base_url + '/resultado/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'mensagem': 'Resultado excluído com sucesso'})


if __name__ == '__main__':
    unittest.main()