#inventory dictionary
inventory = []

#welcome message
print("\n---- Welcome to the Mini Inventory Tracker🛒 ----");
print("===== Please register your Details to create your Inventory =====");
name = input("Enter your name: ");

#validate the user's email
while True:
    user_email = input("Enter your email: ");
    if "@" in user_email and "." in user_email:
        break
    print("Invalid email format, please try again!!")


#start the while loop
while True:
    print("1. Add Item to inventory👾: ")
    print("2. Viw Items in Inventory📝: ")
    print("3. Remove Item🍀: ")
    print("4. Exit❌: ")

    option = input("\nPlease choose an option to continue: ")