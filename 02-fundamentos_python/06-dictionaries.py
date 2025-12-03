user = {
    "name": "Diego",
    "age": 28,
    "email": "diego@mail.com",
    "active": True,
    (19.12, -98.32): "Piedecuesta"
}

user["name"] = "Lionel"
user["country"] = "Bucaramanga"
print(user["name"])
print(user[(19.12, -98.32)])


# VALUES, ITEMS, KEYS
print(user.items())
print(user.keys())
print(user.values())

