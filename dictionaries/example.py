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

peopele = [{
    "name_person": "zeke",
    "age": 12
    },
    {"name_person": "lizel",
    "age": 26
    },
    {
        "name_person": "tom",
        "age": 14
    }
]

for person in peopele:
    name_person = peopele["name_person"]
    age_person = peopele["age"]
    print(f"Hello {name}, you are {age} years old!!")