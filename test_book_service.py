import pytest
from app.api.models import BookIn, BookOut, BookUpdate

book = BookIn(
    name='PSG',
    language='France',
    year=12
)


def test_create_book(book: BookIn = book):
    assert dict(book) == {'name': book.name,
                          'language': book.language,
                          'year': book.year}


def test_update_book_name(book: BookIn = book):
    book_upd = BookOut(
        name='PSG',
        language=book.language,
        year=book.year,
        id=1
    )
    assert dict(book_upd) == {'name': book.name,
                              'language': book.language,
                              'year': book.year,
                              'id': book_upd.id
                              }


def test_update_book(book: BookIn = book):
    book_upd = BookOut(
        name=book.name,
        language=book.language,
        year=book.year,
        id=1
    )
    assert dict(book_upd) == {'name': book.name,
                              'language': book.language,
                              'year': book.year,
                              'id': book_upd.id}
