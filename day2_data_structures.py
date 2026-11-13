api_users = [
    {"id": 1, "name": "Aarav", "role": "admin", "active": True},
    {"id": 2, "name": "Sneha", "role": "user", "active": False},
    {"id": 3, "name": "Vikram", "role": "user", "active": True},
    {"id": 4, "name": "Sneha", "role": "user", "active": True},
    {"id": 5, "name": "Meera", "role": "editor", "active": True},
]

isActive = [user["name"] for user in api_users if user["active"] == True]
print(isActive)

uniq_users = {user["name"] for user in api_users}
print(uniq_users)

isActive_userID = {user["id"]:user["role"] for user in api_users if user["active"]==True}
print(isActive_userID)