import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '356b7122ef0fe0854ca0ea2962decb3b'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "T-300",
    "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']
print(pokemon_id)

body_change = {
    "pokemon_id": pokemon_id,
    "name": "Nastya",
    "photo_id": -1
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_add_pokeball = {
    "pokemon_id": pokemon_id
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

