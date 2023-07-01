# Bem-vindo ao Sistema de Avaliacao do ENADE!

## Configurando o ambiente:

### Requisitos: 
- Python >= 3.9
- [Poetry](https://python-poetry.org/docs/#installation) (Para instalar as dependencias do projeto; Se nao conseguir instalar ou configurar o Poetry, va no arquivo `pyproject.toml` e instale as dependencias do projeto manualmente atraves do comando pip install)

### Instalando as dependencias:
- Abra a pasta raiz onde esta todo o arquivo pyproject.toml e execute os seguintes comandos no terminal:

- Para criar um ambiente virtual e instalar as dependencias nele:
```bash
poetry shell
```
- Para instalar todas as dependencias do projeto:
```bash
poetry install
```

Obs: Caso nao consiga instalar o Poetry corretamente, va no arquivo `pyproject.toml` e instale as dependencias do projeto manualmente atraves do comando pip install no terminal.
  
## Executando a aplicacao

### Requisitos: 
- Python >= 3.9
- Dependencias do projeto instaladas
- MySQL 8

### Definindo as credenciais do DataBase

- Vá ate o arquivo `sistema_avaliacao/credenciais_db.py` e insira as credenciais do seu database.

Obs: se quiser testar a conexao, va no arquivo `user_tests/teste_conexao.py`, insira as credenciais e teste.

### Inicializando aplicacao:
- Na pasta raiz do projeto, execute o seguinte comando no terminal para iniciar a aplicacao:
```bash
python sistema_avaliacao/app.py
```
- Armazene o link que esta aparecendo no terminal para colocarmos ele na variavel base_url. Ele vai se parecer com `http://127.0.0.1:5000` ou `http://localhost:5000`
### Uso da aplicacao:
- Com a aplicacao em execucao, agora é possivel executar comandos que consomem ela em varias linguagens ou ate mesmo no terminal. No exemplo abaixo iremos utilizar o Python e a biblioteca requests para fazer um comando de POST, GET, PUT e DELETE dentro da aplicacao que foi criada.
- Crie um arquivo com a extencao `.py` para inserir os codigos:
  - Defina na variavel `base_url` o link extraido do terminal que foi solicitado acima.
```python
base_url = 'http://localhost:5000'
```
  - POST (para criar um novo usuario):
```python
def post(endpoint, data):
    url = f'{base_url}/{endpoint}'
    response = requests.post(url, json=data)
    return response.json()
data = {
        'id': 1,
        'nome': 'otavio',
        'email': 'otavio@example.com',
        'senha': 'senha123',
        'id_tipo_usuario': 2
    }
    response = post('usuario', data)
    print(response)
```

- GET (para retornar o usuario com base em sua ID):
```python
def get(endpoint):
    url = f'{base_url}/{endpoint}'
    response = requests.get(url)
    return response.json()
user_id = 1
response = get(f'usuario/{user_id}')
print(response)
```

- PUT (para atualizar o cadastro do usuario com base na sua ID):
```python
def put(endpoint, data):
    url = f'{base_url}/{endpoint}'
    response = requests.put(url, json=data)
    return response.json()
user_id = 1
data = {
    'nome': 'Otavio Oliveira',
    'email': 'otavio@example.com',
    'senha': 'senha123',
    'id_tipo_usuario': 2
}
response = put(f'usuario/{user_id}', data)
print(response)
```

- Delete (deletar algum usuario com base em sua ID):
```python
def delete(endpoint):
    url = f'{base_url}/{endpoint}'
    response = requests.delete(url)
    return response.json()
user_id = 1
response = delete(f'usuario/{user_id}')
print(response)
```

Obs: os mesmos comandos podem ser redirecionados a outros objetos do banco de dados, basta indica-los depois do base_url (exemplo: `http://localhost:5000/tipoquestao`).

### Endpoints disponiveis na aplicacao:
| Endpoint     |
|--------------|
| tipoquestao  |
| tipousuario  |
| prova        |
| usuario      |
| questao      |
| provaquestao |
| resultado    |