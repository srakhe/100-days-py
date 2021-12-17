from rental_data_handler import RentalDataHandler
from form_data_handler import FormDataHandler

rentalHandlerObj = RentalDataHandler()
formHandlerObj = FormDataHandler()

property_prices, property_addresses, property_links = rentalHandlerObj.get_rental_properties()
for price, address, link in zip(property_prices, property_addresses, property_links):
    formHandlerObj.submit_form(price, address, link)

formHandlerObj.driver.quit()
