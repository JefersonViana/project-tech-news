from tech_news.database import search_news  # , db
from datetime import datetime

# array = [
#     {
#         "url": "https://blog.betrybe.com/novidades/noticia-bacana",
#         "title": "Notícia bacana",
#         "writer": "Eu",
#         "summary": "Algo muito bacana aconteceu",
#         "reading_time": 4,
#         "timestamp": "04/04/2021",
#         "category": "Ferramentas",
#     },
#     {
#         "url": "https://blog.betrybe.com/novidades/noticia-legal",
#         "title": "Notícia bacana 2",
#         "writer": "Você",
#         "summary": "Algo muito bacana aconteceu de novo",
#         "reading_time": 1,
#         "timestamp": "07/04/2022",
#         "category": "Novidades",
#     }
# ]
# db.news.delete_many({})
# db.news.insert_many(array)


# Requisito 7
def search_by_title(title):
    result = [
        (new['title'], new['url'])
        for new in search_news({'title': {'$regex': title, '$options': 'i'}})
    ]
    return result


# Requisito 8
def search_by_date(date):
    try:
        data_datetime = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError('Data inválida')

    data_formatada = data_datetime.strftime('%d/%m/%Y')
    result = [
        (new['title'], new['url'])
        for new in search_news({'timestamp': data_formatada})
    ]
    return result


# test = search_by_date('21-12-1980')
# print(test)
# print(len(test))


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
