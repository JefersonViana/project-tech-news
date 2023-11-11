from tech_news.database import db

# COPIAR NEWS DE TESTS PARA ech_news.analyzer
# from tech_news.analyzer.news import NEWS
# db.news.delete_many({})
# db.news.insert_many(NEWS)


# Requisito 10
def top_5_categories():
    pipeline = [
        {
            "$group": {
                "_id": "$category",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {
                "count": -1,
                "_id": 1
            }
        },
        {
            "$project": {
                "_id": 0,
                "category": "$_id"
            }
        }
    ]
    result = db.news.aggregate(pipeline)
    categories = [doc["category"] for doc in result]
    return categories[:5]


# print(top_5_categories())
