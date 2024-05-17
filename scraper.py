import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("MARKET_TOKEN")

QUOTE = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"
parameters = {
    "id": 11419,
    "convert": "USD"
}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": TOKEN,
}

session = requests.session()


def get_price() -> str:
    response = session.get(QUOTE, headers=headers, params=parameters)
    data = json.loads(response.text)
    price = data["data"]["11419"]["quote"]["USD"]["price"]
    return price
