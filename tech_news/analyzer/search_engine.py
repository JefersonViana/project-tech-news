from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    result = [
        (new['title'], new['url'])
        for new in search_news({'title': {'$regex': title, '$options': 'i'}})
    ]
    return result


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
