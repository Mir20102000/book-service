import pytest
from app.api.models import BookIn, BookOut, BookUpdate

book = BookIn(
    name='Bible',
    language='Russian',
    year=2000
)


def test_create_book(book: BookIn = book):
    assert dict(book) == {'name': book.name,
                          'language': book.language,
                          'year': book.year}


def test_update_book_name(book: BookIn = book):
    book_upd = BookOut(
        name='Bible',
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
