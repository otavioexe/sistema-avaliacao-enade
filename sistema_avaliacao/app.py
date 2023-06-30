from flask import Flask, jsonify, request
from controllers import (TipoQuestaoController, TipoUsuarioController,
                         ProvaController, UsuarioController,
                         QuestaoController, ProvaQuestaoController,
                         ResultadoController)

# Criando o objeto Flask
app = Flask(__name__)

# Criando instâncias dos controllers
tipo_questao_controller = TipoQuestaoController()
tipo_usuario_controller = TipoUsuarioController()
prova_controller = ProvaController()
usuario_controller = UsuarioController()
questao_controller = QuestaoController()
prova_questao_controller = ProvaQuestaoController()
resultado_controller = ResultadoController()

#------------------------------------------------

# Definindo as rotas para cada CRUD

# Rotas para TipoQuestaoController
@app.route('/tipoquestao', methods=['POST'])
def criar_tipo_questao():
    dados_tipo_questao = request.json
    tipo_questao_controller.criar_tipo_questao(dados_tipo_questao['id'], dados_tipo_questao['nome'])
    return jsonify({'mensagem': 'Tipo de questão criado com sucesso'}), 201

@app.route('/tipoquestao/<int:id_tipo_questao>', methods=['GET'])
def recuperar_tipo_questao(id_tipo_questao):
    tipo_questao = tipo_questao_controller.recuperar_tipo_questao(id_tipo_questao)
    if tipo_questao:
        return jsonify(tipo_questao)
    return jsonify({'mensagem': 'Tipo de questão não encontrado'}), 404

@app.route('/tipoquestao/<int:id_tipo_questao>', methods=['PUT'])
def atualizar_tipo_questao(id_tipo_questao):
    dados_tipo_questao = request.json
    tipo_questao_controller.atualizar_tipo_questao(id_tipo_questao, dados_tipo_questao['nome'])
    return jsonify({'mensagem': 'Tipo de questão atualizado com sucesso'}), 200

@app.route('/tipoquestao/<int:id_tipo_questao>', methods=['DELETE'])
def excluir_tipo_questao(id_tipo_questao):
    tipo_questao_controller.excluir_tipo_questao(id_tipo_questao)
    return jsonify({'mensagem': 'Tipo de questão excluído com sucesso'}), 200

#------------------------------------------------

# Rotas para TipoUsuarioController
@app.route('/tipousuario', methods=['POST'])
def criar_tipo_usuario():
    dados_tipo_usuario = request.json
    tipo_usuario_controller.criar_tipo_usuario(dados_tipo_usuario['id'], dados_tipo_usuario['nome'])
    return jsonify({'mensagem': 'Tipo de usuário criado com sucesso'}), 201

@app.route('/tipousuario/<int:id_tipo_usuario>', methods=['GET'])
def recuperar_tipo_usuario(id_tipo_usuario):
    tipo_usuario = tipo_usuario_controller.recuperar_tipo_usuario(id_tipo_usuario)
    if tipo_usuario:
        return jsonify(tipo_usuario)
    return jsonify({'mensagem': 'Tipo de usuário não encontrado'}), 404

@app.route('/tipousuario/<int:id_tipo_usuario>', methods=['PUT'])
def atualizar_tipo_usuario(id_tipo_usuario):
    dados_tipo_usuario = request.json
    tipo_usuario_controller.atualizar_tipo_usuario(id_tipo_usuario, dados_tipo_usuario['nome'])
    return jsonify({'mensagem': 'Tipo de usuário atualizado com sucesso'}), 200

@app.route('/tipousuario/<int:id_tipo_usuario>', methods=['DELETE'])
def excluir_tipo_usuario(id_tipo_usuario):
    tipo_usuario_controller.excluir_tipo_usuario(id_tipo_usuario)
    return jsonify({'mensagem': 'Tipo de usuário excluído com sucesso'}), 200

#------------------------------------------------

# Rotas para ProvaController
@app.route('/prova', methods=['POST'])
def criar_prova():
    dados_prova = request.json
    prova_controller.criar_prova(dados_prova['id'], dados_prova['data'])
    return jsonify({'mensagem': 'Prova criada com sucesso'}), 201

@app.route('/prova/<int:id_prova>', methods=['GET'])
def recuperar_prova(id_prova):
    prova = prova_controller.recuperar_prova(id_prova)
    if prova:
        return jsonify(prova)
    return jsonify({'mensagem': 'Prova não encontrada'}), 404

@app.route('/prova/<int:id_prova>', methods=['PUT'])
def atualizar_prova(id_prova):
    dados_prova = request.json
    prova_controller.atualizar_prova(id_prova, dados_prova['data'])
    return jsonify({'mensagem': 'Prova atualizada com sucesso'}), 200

@app.route('/prova/<int:id_prova>', methods=['DELETE'])
def excluir_prova(id_prova):
    prova_controller.excluir_prova(id_prova)
    return jsonify({'mensagem': 'Prova excluída com sucesso'}), 200

#------------------------------------------------

# Rotas para UsuarioController
@app.route('/usuario', methods=['POST'])
def criar_usuario():
    dados_usuario = request.json
    usuario_controller.criar_usuario(dados_usuario['id'], dados_usuario['nome'], dados_usuario['email'], dados_usuario['senha'], dados_usuario['id_tipo_usuario'])
    return jsonify({'mensagem': 'Usuário criado com sucesso'}), 201

@app.route('/usuario/<int:id_usuario>', methods=['GET'])
def recuperar_usuario(id_usuario):
    usuario = usuario_controller.recuperar_usuario(id_usuario)
    if usuario:
        return jsonify(usuario)
    return jsonify({'mensagem': 'Usuário não encontrado'}), 404

@app.route('/usuario/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    dados_usuario = request.json
    usuario_controller.atualizar_usuario(id_usuario, dados_usuario['nome'], dados_usuario['email'], dados_usuario['senha'], dados_usuario['id_tipo_usuario'])
    return jsonify({'mensagem': 'Usuário atualizado com sucesso'}), 200

@app.route('/usuario/<int:id_usuario>', methods=['DELETE'])
def excluir_usuario(id_usuario):
    usuario_controller.excluir_usuario(id_usuario)
    return jsonify({'mensagem': 'Usuário excluído com sucesso'}), 200

#------------------------------------------------

# Rotas para QuestaoController
@app.route('/questao', methods=['POST'])
def criar_questao():
    dados_questao = request.json
    questao_controller.criar_questao(dados_questao['id'], dados_questao['descricao'], dados_questao['alternativaA'], dados_questao['alternativaB'], dados_questao['alternativaC'], dados_questao['alternativaD'], dados_questao['alternativaE'], dados_questao['questaoCorreta'], dados_questao['estado'], dados_questao['id_tipo_questao'])
    return jsonify({'mensagem': 'Questão criada com sucesso'}), 201

@app.route('/questao/<int:id_questao>', methods=['GET'])
def recuperar_questao(id_questao):
    questao = questao_controller.recuperar_questao(id_questao)
    if questao:
        return jsonify(questao)
    return jsonify({'mensagem': 'Questão não encontrada'}), 404

@app.route('/questao/<int:id_questao>', methods=['PUT'])
def atualizar_questao(id_questao):
    dados_questao = request.json
    questao_controller.atualizar_questao(id_questao, dados_questao['descricao'], dados_questao['alternativaA'], dados_questao['alternativaB'], dados_questao['alternativaC'], dados_questao['alternativaD'], dados_questao['alternativaE'], dados_questao['questaoCorreta'], dados_questao['estado'], dados_questao['id_tipo_questao'])
    return jsonify({'mensagem': 'Questão atualizada com sucesso'}), 200

@app.route('/questao/<int:id_questao>', methods=['DELETE'])
def excluir_questao(id_questao):
    questao_controller.excluir_questao(id_questao)
    return jsonify({'mensagem': 'Questão excluída com sucesso'}), 200

#------------------------------------------------

# Rotas para ProvaQuestaoController
@app.route('/provaquestao', methods=['POST'])
def adicionar_questao_prova():
    dados_prova_questao = request.json
    prova_questao_controller.adicionar_questao_na_prova(dados_prova_questao['id_prova'], dados_prova_questao['id_questao'])
    return jsonify({'mensagem': 'Questão adicionada à prova com sucesso'}), 201

@app.route('/provaquestao/<int:id_prova>/<int:id_questao>', methods=['DELETE'])
def remover_questao_prova(id_prova, id_questao):
    prova_questao_controller.remover_questao_da_prova(id_prova, id_questao)
    return jsonify({'mensagem': 'Questão removida da prova com sucesso'}), 200

@app.route('/provaquestao/<int:id_prova>/<int:id_questao>', methods=['PUT'])
def atualizar_questao_prova(id_prova, id_questao):
    dados_prova_questao = request.json
    prova_questao_controller.atualizar_questao_na_prova(id_prova, id_questao, dados_prova_questao['nova_questao'])
    return jsonify({'mensagem': 'Questão atualizada na prova com sucesso'}), 200

@app.route('/provaquestao/<int:id_prova>/<int:id_questao>', methods=['GET'])
def recuperar_questao_prova(id_prova, id_questao):
    questao_prova = prova_questao_controller.recuperar_questoes_da_prova(id_prova)
    if questao_prova:
        return jsonify(questao_prova)
    return jsonify({'mensagem': 'Questão não encontrada na prova'}), 404


#------------------------------------------------

# Rotas para ResultadoController
@app.route('/resultado', methods=['POST'])
def criar_resultado():
    dados_resultado = request.json
    resultado_controller.criar_resultado(dados_resultado['id'], dados_resultado['id_prova'], dados_resultado['id_usuario'], dados_resultado['nota'])
    return jsonify({'mensagem': 'Resultado criado com sucesso'}), 201

@app.route('/resultado/<int:id_resultado>', methods=['GET'])
def recuperar_resultado(id_resultado):
    resultado = resultado_controller.recuperar_resultado(id_resultado)
    if resultado:
        return jsonify(resultado)
    return jsonify({'mensagem': 'Resultado não encontrado'}), 404

@app.route('/resultado/<int:id_resultado>', methods=['PUT'])
def atualizar_resultado(id_resultado):
    dados_resultado = request.json
    resultado_controller.atualizar_resultado(id_resultado, dados_resultado['nota'])
    return jsonify({'mensagem': 'Resultado atualizado com sucesso'}), 200

@app.route('/resultado/<int:id_resultado>', methods=['DELETE'])
def excluir_resultado(id_resultado):
    resultado_controller.excluir_resultado(id_resultado)
    return jsonify({'mensagem': 'Resultado excluído com sucesso'}), 200

#------------------------------------------------

# Execute o aplicativo Flask
if __name__ == '__main__':
    app.run()