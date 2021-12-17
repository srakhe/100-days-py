from bs4 import BeautifulSoup

# import lxml if html parser doesnt work

with open('index.html', 'r+') as web_file:
    contents = web_file.read()

soup_obj = BeautifulSoup(contents, 'html.parser')

print(soup_obj.title)
print(soup_obj.title.name)
print(soup_obj.title.string)

print(soup_obj)
print(soup_obj.prettify())

print(soup_obj.a)  # Returns the first of the tag that it finds in the web page.

print(soup_obj.find_all(name='a'))  # Returns all anchor tags
for links in soup_obj.find_all(name='a'):
    print(links.getText())  # Returns the string of the link
    print(links.get('href'))  # Returns only the links!

print(soup_obj.find(name='h1', id='name'))

print(soup_obj.find(name='p', class_='skills'))  # NOTE: Used class_ not class here

# Ability to use CSS selectors in Beautiful Soup:
print(soup_obj.select_one(selector='p a').text)
print(soup_obj.select_one(selector='#name'))  # ID selector
print(soup_obj.select_one('.heading'))  # Class selector
