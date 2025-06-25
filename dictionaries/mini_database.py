#first define the list to store the users we will add
users = [];

print("\n====== Welcome to the Mini Database 👾 ======")

#start the loop 
while True:
    print("\n==== Add New User🙋🏻‍♀️ =====");

    #ask the user for these inputs
    name = input("Enter name: ");
    age = int(input("Enter age: "));
    city = input("Enter City: ");
    role = input("Enter role (admin/user): ");

    #creating the dictionary
    user = {
        "name": name,
        "age": age,
        "city": city,
        "role": role
    }

    #adding the user to the list