#first things first creating empty list to store people's details
users = []

#starting off with a welcome a welcome message
print("--- Welcome to the Mini Database ---")

#creating a while loop thats gonna run when the user wants to continue adding more people
while True:
    print("--- Add New User👾 ---");

    name = input("Enter your name: ");
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "));
    phone_number = int(input("Enter phone number: "))
    
    #get email and validate it
    while True:
        email = input("Enter email: ")
        if "@" in email and "." in email:
            break
        print("Invalid email format, try again")

    
