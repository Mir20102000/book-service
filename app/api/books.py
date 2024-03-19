from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import BookOut, BookIn, BookUpdate
from app.api import db_manager

books = APIRouter()

@books.post('/', response_model=BookOut, status_code=201) #localhost:8002/api/v1/books
async def create_book(payload: BookIn):
    book_id = await db_manager.add_book(payload)

    response = {
        'id': book_id,
        **payload.dict()
    }

    return response


@books.get('/', response_model=List[BookOut]) #localhost:8001/api/v1/characters
async def get_books():
    return await db_manager.get_all_book()