import requests

base_url = 'http://127.0.0.1:5000' 

def get(endpoint):
    url = f'{base_url}/{endpoint}'
    response = requests.get(url)
    return response.json()

def post(endpoint, data):
    url = f'{base_url}/{endpoint}'
    response = requests.post(url, json=data)
    return response.json()

def put(endpoint, data):
    url = f'{base_url}/{endpoint}'
    response = requests.put(url, json=data)
    return response.json()

def delete(endpoint):
    url = f'{base_url}/{endpoint}'
    response = requests.delete(url)
    return response.json()

#------------------------------------------


def test_create_user():
    data = {
        'id': 1,
        'nome': 'tassio',
        'email': 'tassio@example.com',
        'senha': 'senha123',
        'id_tipo_usuario': 2
    }
    response = post('usuario', data)
    print(response)


def test_get_user():
    user_id = 1
    response = get(f'usuario/{user_id}')
    print(response)


def test_update_user():
    user_id = 1
    data = {
        'nome': 'Tassio2',
        'email': 'tassio2@example.com',
        'senha': 'senha123',
        'id_tipo_usuario': 1
    }
    response = put(f'usuario/{user_id}', data)
    print(response)


def test_delete_user():
    user_id = 1
    response = delete(f'usuario/{user_id}')
    print(response)


#test_create_user()
#test_get_user()
#test_update_user()
#test_delete_user()
