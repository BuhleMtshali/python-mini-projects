#inventory dictionary
inventory = []

#welcome message
print("\n---- Welcome to the Mini Inventory Tracker🛒 ----");
print("===== Please register your Details to create your Inventory👥 =====");
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

    option = input(f"\n{name} Please choose an option to continue: ");

    if option == "1":
        product_name = input("Enter the name of product: ");
        product_quantity = int(input("Enter product quantity: "));
        product_price = float(input("Enter the price of the product(each) in rands: "));
        total_price = float(product_price * product_quantity);

        