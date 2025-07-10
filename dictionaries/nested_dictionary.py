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