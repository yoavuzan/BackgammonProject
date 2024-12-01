from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random

class User(BaseModel):
    name: str

users:List[User] = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/updateUsers")
def create_user(user:User):
    print(user)
    for existing_user in users:
        if existing_user.name == user.name:
            return {"status": "User already exists"}
    
    users.append(user)
    return {"status": "User added", "user": user}

@app.get("/getUsers")
def get_users(username:str = None):
    print(username)
    if username:
        for user in users:
            if user.name == username:
                return {"exist": True}
        return {"users": users}
    return {"users": users}

@app.get("/Random")
def randNumber(start:int, end:int):
    return {f"The random number between {start}  to {end} is":random.randint(start, end)}