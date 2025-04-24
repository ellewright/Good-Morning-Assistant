import datetime
import requests
import random

def get_random_pokemon_data():  
    pokemon_list_url = "https://pokeapi.co/api/v2/pokemon-species"
    pokemon_list_response = requests.get(pokemon_list_url)
    pokemon_count = pokemon_list_response.json()["count"]

    url = f"https://pokeapi.co/api/v2/pokemon-species/{random.randint(1, pokemon_count)}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        pokemon_name = pokemon["name"]
        french_name = pokemon["names"][4]["name"]
        print(f"Today's random Pokemon fact is {pokemon_name}, or {french_name} in French.")
    else:
        print("There was an error loading Pokemon data.")

def main():
    current = str(datetime.date.today())
    current_month = current[5:7]
    current_day = current[8:]

    trivia_url = f"http://numbersapi.com/{current_month}/{current_day}"
    trivia_response = requests.get(trivia_url)

    if trivia_response.status_code == 200:
        trivia_fact = trivia_response.text

        print(f"Good morning! Today's date is {current}.")
        print(trivia_fact)
    else:
        print("There was an error. Please try again.")

    get_random_pokemon_data()

main()