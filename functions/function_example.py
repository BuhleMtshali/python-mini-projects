def greet_user(name='stranger'):
    """Displaying a simple greeting"""
    print(f"hello {name.title()}, this is my first function.")

greet_user('buhle')
greet_user()

#favorite book function
def fav_book(name, book_name, book_author):
    """Displaying user favorite book"""
    print(f"Hey, my name is {name.title()} and my favorite book is {book_name.title()} by {book_author.title()}")

fav_book('buhle','the mummy', 'brad pitt')