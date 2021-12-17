import json
import scraper
import notifier


def track():
    with open('prices.json', 'r+') as products:
        products_data = json.load(products)

    for each_product, each_product_data in products_data.items():
        print('Tracking for ', each_product)
        product_url = each_product_data['url']
        product_compare_price = each_product_data['price_to_track']
        product_notify = each_product_data['email']
        scraped_price = scraper.scrape_for_price(product_url)
        if scraped_price <= product_compare_price:
            notifier.send_email(receiver=product_notify, product_name=each_product, deal_price=scraped_price,
                                url=product_url)


def add_new():
    product_name = input('Set a name to the product:\n')
    product_url = input('Enter the url of the product to track:\n')
    product_compare_price = input('Enter the price to compare:\n')
    product_email = input('Enter the email address to notify:\n')
    new_dict = {
        product_name: {
            "url": product_url,
            "price_to_track": float(product_compare_price),
            "email": product_email
        }
    }
    with open('prices.json', 'r+') as products:
        products_data = json.load(products)
    products_data.update(new_dict)
    with open('prices.json', 'w') as products:
        json.dump(products_data, products, indent=4)
