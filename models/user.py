from sqlalchemy import Table,Column, Integer, String
from config.db import meta

users = Table(
    'users',meta,
    Column('id', Integer, primary_key = True, index = True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255))
)
