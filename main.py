import datetime
import requests

def main():
    current = str(datetime.date.today())
    current_month = current[5:7]
    current_day = current[8:]

    url = f"http://numbersapi.com/{current_month}/{current_day}"
    response = requests.get(url)

    if response.status_code == 200:
        trivia_fact = response.text
        print(f"Good morning! Today's date is {current}.")
        print(trivia_fact)
    else:
        print("There was an error. Please try again.")

main()