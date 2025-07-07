example_dictionary = [{'name': 'buhle', 'age': 23, 'profession': 'junior software developer'},
                      {'name': 'zac', 'age': 30, 'profession': 'senior software developer'},
                      {'name': 'linda', 'age': 27, 'profession': 'ui/ux designer'}]

#looping through the list of dictionary
for person in example_dictionary:
    print('New Person: ')
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")
    
favorite_language = {
    'jane': 'dancing',
    'luke': 'reading',
    'jake': 'playing piano',
    'buhle': 'cycling'
}

#creating a for loop
for key, value in favorite_language.items():
    print('=======Favourite Languages==========')
    print(f"{key.capitalize()}: {value.capitalize()}")