users = [
    {
        "name": "buhle",
        "age": 23,
        "city": "durban",
        "role": "admin"
     },
     {
         "name": "luke",
         "age": 16,
         "city": "cape town",
         "role": "user"
     },
     {
         "name": "zakes",
         "age": 65,
         "city": "joburg",
         "role": "user"
     }
    ]

for user in users:
    name = user["name"];
    age = user["age"];
    city = user["city"];
    role = user["role"];
    if role == "admin":
        print(f"{name} is admin");
    else:
        print(f"Hello {name}, you're our current users.")

