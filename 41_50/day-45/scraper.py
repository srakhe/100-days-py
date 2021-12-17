import requests
from bs4 import BeautifulSoup

news_page = requests.get('https://news.ycombinator.com/')
soup_obj = BeautifulSoup(news_page.text, 'html.parser')

news_titles = []
news_links = []
news_scores = []

for a_tags, each_score in zip(soup_obj.find_all(name='a', class_='storylink'),
                              soup_obj.find_all(name='span', class_='score')):
    news_titles.append(a_tags.getText())
    news_links.append(a_tags.get('href'))
    news_scores.append(int(str(each_score.getText()).split(' ')[0]))

max_score = max(news_scores)
max_score_news_title = news_titles[news_scores.index(max_score)]
max_score_news_link = news_links[news_scores.index(max_score)]

print(f'Score: {max_score}\nTitle: {max_score_news_title}\nLink(s): {max_score_news_link}')
