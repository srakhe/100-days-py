import pandas
from bs4 import BeautifulSoup

with open('index.html', 'r+') as web_file:
    movies_website = web_file.read()

web_soup_obj = BeautifulSoup(movies_website, 'html.parser')

movies_list = []
titles_list = web_soup_obj.find_all(name='h3', class_='jsx-2692754980')
for title in titles_list:
    movie_title = str(title.getText()).split(' ', 1)[1]
    movies_list.append(movie_title)

pandas.DataFrame(data=movies_list).to_csv('movies.csv', header=['Movies'], index=True, index_label='Sr. No.',
                                          mode='a')
