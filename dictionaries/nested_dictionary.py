pizza = {
    'jane': ['chicken', 'cheese'],
    'john': ['vegetarian', 'extra mushrooms', 'extra onion'],
    'kate': ['no toppings'],
    'mike': ['chicken', 'mushroom', 'burger pizza', 'beef']
}

#first loop in the dictionary
for name, toppings in pizza.items():
    print(f"{name.title()}'s favorite pizza toppings are: ")
    for topping in toppings:
        print(f"{topping.title()}")