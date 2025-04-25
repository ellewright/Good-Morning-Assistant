import datetime
import requests
import random

def format_month(month):
    match month:
        case "01":
            month = "January"
        case "02":
            month = "February"
        case "03":
            month = "March"
        case "04":
            month = "April"
        case "05":
            month = "May"
        case "06":
            month = "June"
        case "07":
            month = "July"
        case "08":
            month = "August"
        case "09":
            month = "September"
        case "10":
            month = "October"
        case "11":
            month = "November"
        case "12":
            month = "December"

    return month

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

def get_trivia_data():
    current = str(datetime.date.today())
    current_year = current[0:4]
    current_month = current[5:7]
    current_day = current[8:]

    formatted_month = format_month(current_month)

    trivia_url = f"http://numbersapi.com/{current_month}/{current_day}"
    trivia_response = requests.get(trivia_url)

    if trivia_response.status_code == 200:
        trivia_fact = trivia_response.text

        print(f"Good morning! Today's date is {formatted_month} {current_day}, {current_year}.")
        print(trivia_fact)
    else:
        print("There was an error. Please try again.")

def main():
    get_trivia_data()
    get_random_pokemon_data()

main()