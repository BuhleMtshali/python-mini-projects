people = [
    {
        "name": "buhle",
        "age": 23,
        "city": "durban"
     },
     {
         "name": "luke",
         "age": 16,
         "city": "cape town"
     },
     {
         "name": "zakes",
         "age": 65,
         "city": "joburg"
     }
    ]

for person in people:
    name = person["name"];
    age = person["age"];
    city = person["city"];
    print(f"Hi I'm {name}, I'm currently {age} years old and I currently live in {city}")