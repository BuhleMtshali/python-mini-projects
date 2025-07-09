# inventory list
inventory = []

# welcome message
print("\n==== Welcome to the Mini Inventory Tracker🛒 =====")
print("===== Please register your Details to create your Inventory👥 =====")
name = input("Enter your name: ")

# validate the user's email
while True:
    user_email = input("Enter your email: ")
    if "@" in user_email and "." in user_email:
        break
    print("❌ Invalid email format, please try again!")

# start the main menu loop
while True:
    print("\n=== Menu ===")
    print("1. Add Item to Inventory 👾")
    print("2. View Items in Inventory 📝")
    print("3. Remove Item 🍀")
    print("4. Exit ❌")

    option = input(f"\n{name}, please choose an option to continue: ")

    if option == "1":
        while True:
            product_name = input("Enter the name of product: ")
            product_quantity = int(input("Enter product quantity: "))
            product_price = float(input("Enter the price of the product(each) in Rands: "))
            total_price = product_price * product_quantity

            # creating the product dictionary
            product = {
                "product_name": product_name,
                "product_quantity": product_quantity,
                "product_price": product_price,
                "total_price": total_price
            }

            inventory.append(product)
            print(f"✅ {product_name} successfully added to inventory, {name}!")

            add_more = input("Do you want to add another product? (yes/no): ").lower()
            if add_more != "yes":
                break

    elif option == "2":
        if not inventory:
            print(f"🚫 {name}, your inventory is currently empty. Try adding something first!")
        else:
            print(f"\n==== {name}, here are your inventory items ====")
            
            print(
                    f"""
==== User Info 👥 ====
Name: {name}
Email: {user_email}
--------------------
                    """
                )
            for product in inventory:
                print(f"""
Product Name       : {product["product_name"]}
Product Quantity   : {product["product_quantity"]}
Product Price(each): R{product["product_price"]}
============================
Total Price        : R{product["total_price"]}
============================
""")

    elif option == "3":
        if not inventory:
            print("🚫 Your inventory is empty. Nothing to remove.")
        else:
            remove_item = input("Enter the name of the product you want to remove: ")
            for product in inventory:
                if remove_item.lower() == product["product_name"].lower():
                    inventory.remove(product)
                    print(f"✅ {remove_item} was removed from your inventory!")
                    break
            else:
                print(f"🚫 {remove_item} does not exist in inventory!")

    elif option == "4":
        print(f"👋 Thank you for using the Mini Inventory Tracker, {name}!")
        break

    else:
        print("❌ Invalid option, please choose 1–4.")
