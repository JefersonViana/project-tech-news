# from tech_news.database import db

# COPIAR NEWS DE TESTS PARA ech_news.analyzer
# from tech_news.analyzer.news import NEWS
# db.news.delete_many({})
# db.news.insert_many(NEWS)


# Requisito 10
# def top_5_categories():
# pipeline = [
#     {
#         "$group": {
#             "_id": "$category",
#             "count": {"$sum": 1}
#         }
#     },
#     {
#         "$sort": {
#             "count": -1,
#             "_id": 1
#         }
#     },
#     {
#         "$project": {
#             "_id": 0,
#             "category": "$_id"
#         }
#     }
# ]
# result = db.news.aggregate(pipeline)
# categories = [doc["category"] for doc in result]
# return categories[:5]


# print(top_5_categories())
from tech_news.database import search_news
from collections import Counter
# COPIAR NEWS DE TESTS PARA ech_news.analyzer
# from tech_news.analyzer.news import NEWS
# db.news.delete_many({})
# db.news.insert_many(NEWS)


# Requisito 10
def top_5_categories():
    documents = search_news({})
    category_counter = Counter(doc["category"] for doc in documents)
    sorted_categories = sorted(
        category_counter.keys(),
        key=lambda category: (-category_counter[category], category)
        )
    return sorted_categories[:5]
