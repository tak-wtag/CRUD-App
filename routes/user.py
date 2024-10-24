from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User 

user = APIRouter()

@user.on_event("startup")
def create_table():
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """
    cursor.execute(create_table_query)

@user.post("/{users}")
def posts(user : User):
    cursor = conn.cursor()
    insert_q = "INSERT INTO users(name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_q,(user.name, user.email, user.password))
    conn.commit()
    #conn.close()
    return {"message": "user created"}

@user.get("/users/")
async def read():
    cursor = conn.cursor()
    select_q = "SELECT * from users"
    cursor.execute(select_q, )
    user = cursor.fetchall()
    conn.commit()
    #cursor.close()
    if user:
        return user
    else:
        return {"msg": "Data not available"}

@user.get("/{id}")
def read(id: int):
    cursor = conn.cursor()
    select_q = "SELECT * from users WHERE id = %s"
    cursor.execute(select_q, (id, ))
    user = cursor.fetchone()
    conn.commit()
    #cursor.close()
    if user:
        return user
    else:
        return {"msg": "Data not available"}

@user.put("/user{id}")
def update(id: int, user: User):
    cursor = conn.cursor()
    update_q = "UPDATE users SET name = %s, email = %s, password = %s WHERE id = %s"
    cursor.execute(update_q, (user.name, user.email, user.password, id))
    conn.commit()
    #cursor.close()
    return {"msg": "Values updated"}

@user.delete("/user/{id}")
def delete(id: int):
    cursor = conn.cursor()
    delete_q = "DELETE FROM users WHERE id = %s"
    cursor.execute(delete_q, (id, ))
    conn.commit()
    #cursor.close()
    return {"msg": "Values deleted"}


