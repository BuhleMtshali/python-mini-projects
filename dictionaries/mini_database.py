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

    #create the user dictionary/object
    user = {
        "name": name,
        "last_name": last_name,
        "age": age,
        "phone_number": phone_number,
        "email": email
    }

    #append the user to the array
    users.append(user)

    #ask if the person wants to add more people
    add_more = input("Do you want to add another user? (yes/no): ")

    #decide if the loop continues breaks/continues
    if add_more != "yes":
        print(" ---- kay, done adding users ----")
        break;
print("=== Here is the list of people who have registered: ");
for user in users:
    name = user["name"];
    last_name = user["last_name"];
    age = user["age"];
    phone_number = user["phone_number"];
    email = user["email"]
    print(f"""
    Name: {name}
    Last Name: {last_name}
    Age: {age}
    Phone Number: {phone_number}
    Email: {email}
    """)

    