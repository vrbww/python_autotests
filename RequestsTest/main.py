import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '4b8a16103168edfcdf90e737f7b5dc5f'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_pokemon_create = {
    "name": "generate",
    "photo_id": -1
}
responce_pokemon_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_create) 
print(responce_pokemon_create.text)

pokemon_id = responce_pokemon_create.json()['id']

body_pokemon_change_name = {
    "pokemon_id": pokemon_id,
    "name": "generate",
    "photo_id": -1
}
responce_pokemon_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemon_change_name) 
print(responce_pokemon_change_name.text)

body_pokemon_add_pockeball = {
    "pokemon_id": pokemon_id
}
responce_pokemon_add_pockeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokemon_add_pockeball) 
print(responce_pokemon_add_pockeball.text)