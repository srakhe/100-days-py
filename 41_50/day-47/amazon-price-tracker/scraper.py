import requests
from bs4 import BeautifulSoup


def scrape_for_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(url, headers=headers)
    soup_obj = BeautifulSoup(response.text, 'html.parser')
    price_div = soup_obj.find(name='span', id='priceblock_ourprice')
    price = price_div.getText()[2:].replace(',', '')
    price = float(price)
    return price
