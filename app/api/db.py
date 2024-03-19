import os
from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)
from databases import Database

DATABASE_URI = 'postgresql://secUREusER:StrongEnoughPassword)@51.250.26.59:5432/postgres'

engine = create_engine(DATABASE_URI)
metadata = MetaData()

books = Table(
    'bookmark',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('language', String(20)),
    Column('year', Integer),
)

database = Database(DATABASE_URI)
