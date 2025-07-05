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

        #creating the product dictionary
        product = {
            "product_name": product_name,
            "product_quantity": product_quantity,
            "product_price": product_price,
            "total_price": total_price
        }

        #adding the product to the inventory
        inventory.append(product)

        #ask if the user wants to add more products
        add_more = input("Do you want to add another product? (yes/no): ")

        #decide if the loop breaks or continues
        if add_more != "yes":
            print("✅Successfuly added product to inventory!!!");
            break;
    elif option == "2":
        if len(inventory) > 0:
            print(f'==== {name}, Here are items in your inventory ====')
            for product in inventory:
                name_product = inventory["product_name"];
                quantity = inventory["product_quantity"];
                price = inventory["product_price"];
                total = inventory["total_price"];

                print(f"""
                ==== User Info👥 ====
                Name: {name}
                Email: {user_email}
                --------------------
                Product Name: {name_product}
                Product Quantity: {quantity}
                Product Price(each): {price}
                ============================
                Total Price: R{total}
                ============================
                      """)
            else:
                print(f"{name}, your inventory is currently empty, try adding first")
    elif option == "3":
        remove_item = input("Enter the name of the product you want to remove: ");
        for product in inventory:
            if remove_item in inventory["product_name"]:
                del product
            else:
                print(f"{remove_item} does not exist in inventory!!")
    elif option == "4":
        print(f"Thank you for using the mini inventory app, {name}");
        break;
    else:
        print(f"{option} is not a valid option please try again")

