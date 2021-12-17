from bs4 import BeautifulSoup
import requests


class RentalDataHandler:

    def __init__(self):
        self.url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.83501662207031%2C%22east%22%3A-122.03164137792969%2C%22south%22%3A37.55325083788472%2C%22north%22%3A37.99666720211685%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

    def format_price(self, price):
        price_num = ''
        for char in price:
            if char.isdigit():
                price_num += char
        return int(price_num)

    def get_rental_properties(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8'
        }
        response = requests.get(self.url, headers=headers)
        soup_obj = BeautifulSoup(response.text, 'html.parser')
        all_properties = soup_obj.find_all(name='div', class_='list-card-info')
        property_prices = []
        property_addresses = []
        property_links = []
        for each_property in all_properties:
            link = each_property.a.get('href')
            address = each_property.address.getText()
            price = each_property.find(name='div', class_='list-card-price').getText()
            price = self.format_price(price)
            property_links.append(link)
            property_addresses.append(address)
            property_prices.append(price)
        property_prices, property_addresses, property_links = zip(
            *sorted(zip(property_prices, property_addresses, property_links)))
        return property_prices, property_addresses, property_links
