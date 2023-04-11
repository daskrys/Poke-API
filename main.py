import requests

def get_pokemon_info(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return data
    else:
        print(f"Error: Received status code {response.status_code}")
        
        return None

print('Enter a Pokemon: ')
pokemon = input()
pokemon_data = get_pokemon_info(pokemon)
pokemon_location = requests.get(pokemon_data['location_area_encounters']).json()

if pokemon_data:
    print(f"Name: {pokemon_data['name'].title()}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")

    print("Types:")
    for i in pokemon_data['types']:
        print(f"- {i['type']['name'].title()}")

if pokemon_location:

    print("Location: ")
    for i in pokemon_location:
        print(f"- {i['location_area']['name'].title()}") 