import requests
# from bs4 import BeautifulSoup
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


fetch('https://blog.betrybe.com/')


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
