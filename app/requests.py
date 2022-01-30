from app import app
import requests
from .config import Config
import os
from .models import news_article

News_article = news_article.News_Article

Api_key = os.getenv('API_KEY')
tech_base_url = app.config['TECH_CRUNCH_BASE_URL']
business_base_url=app.config['BUSINESS_BASE_URL']
all_article_base_url= app.config['ALL_ARTICLES_BASE_URL']

def tech_news():
    base_url = tech_base_url.format(Api_key)
    tech_data = requests.get(base_url).json()
    tech_news = []

    for tech in tech_data['articles']:
        id = tech['source']
        title = tech['title']
        poster = tech['urlToImage']
        url_link = tech['url']
        description = tech['description']
        published_date = tech['publishedAt']
        content = tech['content']
        
        tech_object = News_article(id, title, poster, url_link, description, published_date, content)
        tech_news.append(tech_object)
    return tech_news

def all_articles_news():
    '''
    all_articles_news function displays all news from various sources without specification
    '''
    base_url = all_article_base_url.format(Api_key)
    all_article_data = requests.get(base_url).json()
    all_articles = []
    # print(all_article_data['articles'])
# id, poster, url_link, description, published_date, content
    for articles in all_article_data['articles']:
        id = articles['source']
        title = articles['title']
        poster = articles['urlToImage']
        url_link = articles['url']
        description = articles['description']
        published_date = articles['publishedAt']
        content = articles['content']
        
        articles_object = News_article(id, title, poster, url_link, description, published_date, content)
        all_articles.append(articles_object)
    # print(all_articles)

    return all_articles

def business_news():
    '''
    business_news function for getting data about us business operations
    '''
    base_url = business_base_url.format(Api_key)
    bussiness_articles = requests.get(base_url).json()
    business_data = []
    for business in bussiness_articles ['articles']:
        id = business['source']
        title = business['title']
        poster = business['urlToImage']
        url_link = business['url']
        description = business['description']
        published_date = business['publishedAt']
        content = business['content']
        
        articles_object = News_article(id, title, poster, url_link, description, published_date, content)
        business_data .append(articles_object)

    return business_data

