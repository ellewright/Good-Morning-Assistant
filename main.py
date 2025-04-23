import datetime
import requests
import random

def main():
    current = str(datetime.date.today())
    current_month = current[5:7]
    current_day = current[8:]

    trivia_url = f"http://numbersapi.com/{current_month}/{current_day}"
    trivia_response = requests.get(trivia_url)

    poke_url = "https://pokeapi.co/api/v2/pokemon-species"
    poke_response = requests.get(poke_url)

    if trivia_response.status_code == 200 and poke_response.status_code == 200:
        trivia_fact = trivia_response.text
        pokemon_count = poke_response.json()["count"]

        random_pokemon_url = f"https://pokeapi.co/api/v2/pokemon-species/{random.randint(1, pokemon_count)}"
        random_pokemon_response = requests.get(random_pokemon_url)

        print(f"Good morning! Today's date is {current}.")
        print(trivia_fact)

        if random_pokemon_response.status_code == 200:
            random_pokemon = random_pokemon_response.json()
            random_pokemon_name = random_pokemon["name"]
            french_translation = random_pokemon["names"][4]["name"]
            print(f"Today's random Pokemon fact is {random_pokemon_name}, or {french_translation} in French.")
    else:
        print("There was an error. Please try again.")

main()