from fastapi import FastAPI, HTTPException

app = FastAPI()

# Base de datos simulada en memoria
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Eliminamos al usuario
    deleted_user = users.pop(user_id)
    return {"message": "User deleted", "user": deleted_user}
