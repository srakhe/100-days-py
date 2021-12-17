from selenium import webdriver

firefox_driver = '/path/to/geckodriver'

driver = webdriver.Firefox(executable_path=firefox_driver)

driver.get('https://www.amazon.in/HP-Laptop-Windows-Natural-14s-cr2000tu/dp/B08428CSZF')

price_block = driver.find_element_by_id('priceblock_ourprice')
if price_block.text:
    print(price_block.text)
else:
    print('Not found!')

print(driver.find_element_by_xpath('//*[@id="dp-container"]/script[3]'))
# Get the XPath from the inspect of the browser

driver.get('https://www.python.org')

input_block = driver.find_element_by_name('q')
print(input_block.get_attribute('placeholder'))

logo = driver.find_element_by_class_name('python-logo')
print(logo.size)

doc_link = driver.find_element_by_css_selector('.documentation-widget a')
print(doc_link.text)

event_dict = {}
i = 0
counter = 0
event_menu = driver.find_element_by_css_selector('.event-widget ul')
event_menu_list = event_menu.text.split('\n')
for i in range(0, len(event_menu_list), 2):
    date = event_menu_list[i]
    name = event_menu_list[i + 1]
    event_dict[counter] = {"date": date, "name": name}
    counter += 1
print(event_dict)

driver.close()
