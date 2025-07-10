# Nesting a list in a dictionary

pizza = {
    'jane': ['chicken', 'cheese'],
    'john': ['vegetarian', 'extra mushrooms', 'extra onion'],
    'kate': [],
    'mike': ['chicken', 'mushroom', 'burger pizza', 'beef']
}

#first loop in the dictionary
for name, toppings in pizza.items():
    print(f"{name.title()}'s favorite pizza toppings are: ")
    if len(toppings) <= 0:
        print(f"{name}, does not like any toppings on their pizza!!!")
    else:

        for topping in toppings:
            print(f" - {topping.title()}")

#nesting a dictionary in a dictionary
users = {
    'joyce': {
        'first': 'joycen',
        'last': 'cage',
        'location': 'durban',
    },

    'ryan': {
        'first': 'rysalin',
        'last': 'gosling',
        'location': 'dundee'
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")