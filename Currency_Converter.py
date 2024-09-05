import requests
import json

API_KEY="fca_live_vbRtKklMAaNt5eYgWchZrCIZU5JrbtLVE6GF8G1C"
BASE_URL=f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES={ "USD", "CAD", "EUR", "AUD", "CNY"}

def convert_currency(base):
    currencies=", ".join(CURRENCIES)
    url=f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response=requests.get(url)
        data=response.json()
        return data["data"]
    except:
        print("Invalid Currency: ")
        return None

while True:   
    base=input("Enter the base currency: ").upper()

    if base=="Q":
        break
        
    data=convert_currency(base)
    if not data:
        continue

    del data[base]
    for ticker,value in data.items():
        print(f"{ticker}:{value}")    