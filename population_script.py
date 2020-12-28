import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'different.settings')
import django

django.setup()
from bs4 import BeautifulSoup as bs
import requests
from articles.models import Article
from django.contrib.auth.models import User
from django.core.files import File
import os
import json


def find_text():
    url = 'https://www.lipsum.com/feed/html'
    query = requests.get(url).text
    soup = bs(query, 'lxml')
    paragraph = soup.find_all('p')
    result = ''
    for el in paragraph:
        result += el.get_text()
    return result


names = ['Curabitur eget tortor nisl. Fusce.',
         'Ut sem orci, varius vitae.',
         'Pellentesque et eros et quam.',
         'Morbi tempor posuere turpis et.',
         'In ornare magna in sem.',
         'Etiam a justo tincidunt, pharetra.',
         'Nullam nisl sapien, hendrerit egestas.',
         'In sit amet diam semper.',
         'Vivamus nec purus ut libero.',
         'Donec tempor volutpat nisi sit.',
         ]


def find_pic():
    url = 'https://picsum.photos/200/300'
    p = requests.get(url)
    img = requests.get(p.url).content
    return img


def fish():
    url = 'https://fish-text.ru/get?'
    name = requests.get(url + '&type=title&number=1').json()
    article = requests.get(url + '&type=paragraph&number=2').json()
    return [name['text'], article['text']]


def populate():
    i = 0
    print(i)
    while i < 10:
        text = find_text()
        pic = find_pic()
        img_address = 'media/articles/{}.jpg'.format(i)
        with open(img_address, 'wb') as image:
            image.write(pic)
            image.close()
        a = Article.objects.create(title=names[i], description=text, author=User.objects.filter(id=1).first())
        a.img.save(img_address, File(open(img_address, 'rb')))
        os.remove(img_address)
        print(a)
        i += 1


def populate_russian():
    i = 0
    while i < 10:
        article_raw = fish()
        article_title = article_raw[0]
        article_body = article_raw[1]
        pic_raw = find_pic()
        image_address = 'media/articles/{}.jpg'.format(article_title)
        with open(image_address, 'wb') as image:
            image.write(pic_raw)
            image.close()
        article = Article.objects.create(title=article_title, description=article_body, author=
        User.objects.filter(id=1).first())
        article.img.save('{}.jpg'.format(article_title), File(open(image_address, 'rb')))
        os.remove(image_address)
        print(article_title)
        i += 1


if __name__ == '__main__':
    # populate()
    populate_russian()
