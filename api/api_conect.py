import requests

def get_pokemon_details(url):
    response = requests.get(url)
    if response.status_code == 200:
        payload = response.json()
        name = payload.get('name', 'Unknown')
        abilities = [ability['ability']['name'] for ability in payload.get('abilities', [])]
        types = [poke_type['type']['name'] for poke_type in payload.get('types', [])]
        return name, abilities, types
    else:
        print(f"Error al obtener detalles del Pokémon: {response.status_code}")
        return None, None, None

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon', offset=0):
    args = {'offset': offset, 'limit': 20}
    response = requests.get(url, params=args)

    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])

        if results:
            for pokemon in results:
                name, abilities, types = get_pokemon_details(pokemon['url'])
                if name:
                    print(f"Nombre: {name}")
                    print(f"Habilidades: {', '.join(abilities)}")
                    print(f"Tipos: {', '.join(types)}")
                    print('---')

        next_step = input("¿Seguir listando? (y/n): ").lower()
        if next_step == 'y':
            get_pokemons(offset=offset + 20)
    else:
        print(f"Error: {response.status_code}")

if __name__ == '__main__':
    get_pokemons()





# import requests

# def get_pokemons(url='https://pokeapi.co/api/v2/pokemon', offset=0):
#     args = {'offset': offset, 'limit': 20}
#     response = requests.get(url, params=args)

#     if response.status_code == 200:
#         payload = response.json()
#         results = payload.get('results', [])

#         if results:
#             for pokemon in results:
#                 name = pokemon['name']
#                 print(name)
        
#         next_step = input("¿Seguir listando? (y/n): ").lower()
#         if next_step == 'y':
#             get_pokemons(offset=offset + 20)
#     else:
#         print(f"Error: {response.status_code}")

# if __name__ == '__main__':
#     get_pokemons()
