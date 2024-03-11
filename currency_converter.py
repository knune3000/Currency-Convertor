"""Takes in dollar amount and converts it to country of choice."""

import requests

api_url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_uZ84G1zfwrgWecrmEmdMZDOFHqct3emozvynpLTi"

response = requests.get(api_url)
data = response.json()

amount = input("Enter US dollar amount: ")
exchange_country = input("Enter 3 letter symbol for country you want to convert the amount to: ")

conversion_amount = 0.0

for key in data['data']:
    if key == exchange_country:
        conversion_amount = float(amount) * float(data['data'][key])

rounded_amount = str(round(conversion_amount, 2))

print("Your new amount after conversion to " + exchange_country + " is $" + str(rounded_amount))
