import requests

pokemon_number = input("Digite o número do Pokémon: ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"

response = requests.get(url)

if response.status_code == 200:
    # Converte a resposta em JSON
    pokemon_data = response.json()
    # Extrai o nome do Pokémon
    pokemon_name = pokemon_data["name"]
    print(f"O nome do Pokémon número {pokemon_number} é {pokemon_name}.")
else:
    print("Pokémon não encontrado. Por favor, tente com um número diferente.")
