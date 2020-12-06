import requests
import json


def Calculate(basement, other, amount):
    link = f"https://api.exchangeratesapi.io/latest?base={basement}"
    data = requests.get(link)
    data = json.loads(data.text)
    for a in data["rates"]:
        if a == other:
            change = data["rates"][a]
            result = amount * change
            change = "{:.2f}".format(change)
            result = "{:.2f}".format(result)
            print(f"1 {basement} = {change} {other}")
            print(f"{amount} {basement} = {result} {other}")


baselink = "https://api.exchangeratesapi.io/latest?base=USD"
list1 = requests.get(baselink)
list1 = json.loads(list1.text)
while True:
    print("There are the list of currencies:")
    currencies = []
    for a in list1["rates"]:
        currencies.append(a)
    print(currencies)
    basement = input("From: ").upper()
    other = input("To: ").upper()
    amount = int(input("Amount: "))
    Calculate(basement, other, amount)
    question = input("Do you want to convert again: ")
    if question == "no":
        break
