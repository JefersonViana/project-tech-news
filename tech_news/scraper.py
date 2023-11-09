import requests
from parsel import Selector
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        site = requests.get(url, timeout=3,
                            headers={"user-agent": "Fake user-agent"})
        if site.status_code != 200:
            return None
        else:
            return site.text
    except requests.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    if html_content:
        selector = Selector(text=html_content)
        hrefs = selector.css('.cs-overlay-link').xpath('@href').getall()
        return hrefs
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css('.next').xpath('@href').get()
    return next_page


test = scrape_next_page_link(fetch('https://blog.betrybe.com/'))
print(test)
# print(len(test))


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
