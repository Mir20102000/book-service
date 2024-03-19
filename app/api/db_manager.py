from app.api.models import BookIn, BookOut, BookUpdate
from app.api.db import books, database


async def add_book(payload: BookIn):
    query = books.insert().values(**payload.dict())

    return await database.execute(query=query)


async def get_all_book():
    query = books.select()
    return await database.fetch_all(query=query)
