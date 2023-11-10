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


def formated_url(selector: Selector) -> str:
    href = selector.css('link[rel="canonical"]::attr(href)').get()
    if href:
        return href
    return ' '


def formated_title(selector: Selector) -> str:
    title = selector.css('h1.entry-title::text').get()
    if title:
        return title.replace('\xa0', '')
    return ' '


def formated_timestamp(selector: Selector) -> str:
    timestamp = selector.css('li.meta-date::text').get()
    if timestamp:
        return timestamp
    return ' '


def formated_author(selector: Selector) -> str:
    author = selector.css('span.fn a::text').get()
    if author:
        return author.replace('\t', "").replace('\n', "")
    return ' '


def formated_reading_time(selector: Selector) -> int:
    reading_time = selector.css('li.meta-reading-time::text').get()
    if reading_time:
        return int(reading_time.split(' ')[0])
    return 0


def formated_summary(selector: Selector) -> str:
    div = 'div.entry-content'
    summary = selector.css(div).css('p')[0].css('p *::text').getall()
    summary = ''.join(summary).replace('\xa0', '')
    if summary[-1] == ' ':
        return summary[:-1]
    return summary


def formated_category(selector: Selector) -> str:
    category = selector.css('span.label::text').get()
    if category:
        return category
    return ' '


# Requisito 4
def scrape_news(html_content):
    tech_new = {}
    selector = Selector(text=html_content)
    tech_new['url'] = formated_url(selector)
    tech_new['title'] = formated_title(selector)
    tech_new['timestamp'] = formated_timestamp(selector)
    tech_new['writer'] = formated_author(selector)
    tech_new['reading_time'] = formated_reading_time(selector)
    tech_new['summary'] = formated_summary(selector)
    tech_new['category'] = formated_category(selector)
    return tech_new


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
