#first define the list that will hold the added numbers
contact_book = [];

#print the welcome message
welcome_message = "===== 👋🏻Welcome to you own Personalized Contact Book📲 =====";
menu_message = "\n==== Contact Book Menu🔢 ===="
print(welcome_message)

#get the user's details
user_name = input("Enter your name👥: ");
user_lastname = input("Enter your last nameℹ️: ");

#Validating the user's phone number


#validate the email with a while loop
while True:
    user_email = input("Enter your email📧: ")
    if "@" in user_email and "." in user_email:
        break
    print("Invalid email format🚫")

#start the loop for the contact book
while True:
    print(menu_message)
    print("1. Add Contact👤: ")
    print("2. View Contact List👥: ")
    print("3. Delete Contact🗑️: ")
    print("4. Exit❌")
