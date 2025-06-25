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
   for name, age, city in person:
      print(f"{name}, {age}, {city}")