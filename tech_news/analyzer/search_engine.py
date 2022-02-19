from tech_news.database import search_news
from datetime import datetime
# from tech_news.scraper import get_tech_news


def query(key, value):
    regex = {"$regex": value, "$options": "i"}
    query = {key: regex}
    return query


def tupla_title_url(list):
    data = []
    for element in list:
        data.append((element["title"], element["url"]))
    return data


# Requisito 6
def search_by_title(title):
    news_found = search_news(query("title", title))
    return tupla_title_url(news_found)


# Requisito 7
# validar formato da data
# https://docs.python.org/pt-br/3/library/datetime.html#strftime-and-strptime-behavior
def search_by_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    news_found = search_news(query("timestamp", date))
    return tupla_title_url(news_found)


# Requisito 8
def search_by_source(source):
    news_found = search_news(query("sources", source))
    return tupla_title_url(news_found)


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# get_tech_news(15)
# print(search_by_title(
# "Novo radiotelescópio africano vai ajudar a fotografar"))
