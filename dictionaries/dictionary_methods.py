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
friends = ['luke']
#creating a for loop
print('=======Favourite Hobby==========')
for key, value in favorite_language.items():
    
    print(f"{key.capitalize()}: {value.title()}")

languages = {
    'kate': 'python',
    'john': 'c',
    'cindy': 'javascript',
    'luke': 'c'
}

for fav_lang in set(languages.values()):
    print(fav_lang.title())