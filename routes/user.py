from fastapi import APIRouter
from config.db import conn
from models.main import users
from schemas.main import User 

user = APIRouter()

@user.get("/")
async def read():
    return conn.execute(users.select()).fetchall()

@user.get("/")
async def read(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def write(user: User):
    conn.execute(users.insert().values(
        name = user.name,
        email = user.email,
        password = user.password
    ))
    return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def update(id: int, user: User):
    conn.execute(users.update(
        name = user.name,
        email = user.email,
        password = user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.get("/")
async def delete():
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
