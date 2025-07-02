#first things first creating empty list to store people's details
users = []

#starting off with a welcome a welcome message
print("--- Welcome to the Mini Database ---")

#creating a while loop thats gonna run when the user wants to continue adding more people
while True:
    print("--- Add New User👾 ---");

    name = input("Enter your name: ");
    age = int(input("Enter your age: "));
    email = input("Enter your email: ");