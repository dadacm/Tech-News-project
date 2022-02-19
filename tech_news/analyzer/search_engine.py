from tech_news.database import search_news
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
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# get_tech_news(15)
# print(search_by_title(
# "Novo radiotelescópio africano vai ajudar a fotografar"))
