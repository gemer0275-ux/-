import requests
from bs4 import BeautifulSoup
import time
import lxml

link = "https://habr.com/ru/"
response = requests.get(link)
soup =BeautifulSoup(response.text,'lxml')
articles = soup.find_all('article')
for i,article in enumerate(articles[:6], 1):
    title = (article.find('a', class_='tm-title__link') or
             article.find('a', class_='tm-article-snippet__title-link') or
             (article.find('h2').find('a') if article.find('h2') else None))
    user = article.find('a',class_ ='tm-user-info__username')
    time  =article.find('time')
    preview = (article.find('div', class_='article-formatted-body') or
               article.find('div', class_='tm-article-body') or
               article.find('div', class_='tm-article-snippet__lead'))
    print(f"\n--- Статья {i} ---")
    print("Заголовок:", title.text if title else "Не найден")
    print("Автор:", user.text if user else "Не найден")
    print("Время:", time['title'] if time else "Не найден")
    if preview:
        desc = preview.text.strip().replace('\n', ' ')[:200]
        print("Описание:", desc + "...")
    else:
        print("Описание: Нет описания")