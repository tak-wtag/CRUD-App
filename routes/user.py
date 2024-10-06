from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User 

user = APIRouter()

@user.post("/{users}")
def posts(user : User):
    cursor = conn.cursor()
    insert_q = "INSERT INTO users(name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(insert_q,(user.name, user.email, user.password))
    conn.commit()
    #conn.close()
    return {"message": "this is working"}

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


