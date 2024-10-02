from fastapi import FastAPI
from routes.main import user

app = FastAPI()

app.include_router(user)

