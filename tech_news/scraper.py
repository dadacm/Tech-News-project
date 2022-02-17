import requests
import time
from parsel import Selector
import re


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_urls = selector.css(
        "div.tec--list__item a.tec--card__thumb__link::attr(href)").getall()
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_url = selector.css('a.tec--btn::attr(href)').get()
    if next_page_url is None:
        return None

    return next_page_url


# Requisito 4
# regex
# https://pt.stackoverflow.com/questions/254748/remover-caracteres-n%C3%A3o-num%C3%A9ricos-de-uma-string-em-python
# .strip()
# https://pt.stackoverflow.com/questions/107841/fun%C3%A7%C3%A3o-equivalente-ao-trim-fun%C3%A7%C3%A3o-para-remover-espa%C3%A7os-extras-no-in%C3%ADcio-e-fim
def list_format(new_list, list_to_format):
    for element in list_to_format:
        new_list.append(element.strip())


def scrape_noticia(html_content):
    selector = Selector(html_content)
    title_selector = selector.css("h1.tec--article__header__title::text").get()
    url_selector = selector.css("head link[rel=canonical]::attr(href)").get()
    timestamp_selector = selector.css("time::attr(datetime)").get()
    writer_selector = selector.css(
        ".tec--author__info *:first-child *::text").get()
    if writer_selector is None:
        writer_selector = selector.css(
            '.tec--timestamp__item.z--font-bold a::text'
        ).get()

    share_seletor = selector.css("div.tec--toolbar__item::text").get()
    if share_seletor:
        share_seletor = re.sub('[^0-9]', '', share_seletor)

    coments_seletor = selector.css("#js-comments-btn::attr(data-count)").get()

    sumary_selector = selector.css(
        "div.tec--article__body > p:first-child *::text").getall()
    summary = ''
    for tag in sumary_selector:
        summary = summary + tag

    source_selector = selector.css(
        "div.z--mb-16 div a.tec--badge::text").getall()
    source_list = []
    list_format(source_list, source_selector)

    categories_selector = selector.css(
        "#js-categories a.tec--badge::text").getall()
    categories_list = []
    list_format(categories_list, categories_selector)

    return({
        "url": url_selector,
        "title": title_selector,
        "timestamp": timestamp_selector,
        "writer": writer_selector.strip(),
        "shares_count": int(share_seletor) if share_seletor else 0,
        "comments_count": int(coments_seletor) if coments_seletor else 0,
        "summary": summary,
        "sources": source_list,
        "categories": categories_list,
    })


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# noticia = fetch(
#     "https://www.tecmundo.com.br/mobilidade-urbana-smart-cities/155000-musk-tesla-carros-totalmente-autonomos.htm"
#     )
# print(scrape_noticia(noticia))
