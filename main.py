from fastapi import FastAPI

app = FastAPI()

users = []

@app.get("/")
def home():
    return {"message": "API Running"}
@app.post("/aol")
def add_user_alias(user: dict):
    users.append(user)
    return {"message": "User added"}
@app.post("/add_user")
def add_user(user: dict):
    users.append(user)
    return {"message": "User added"}

@app.get("/users")
def get_users():
    return users