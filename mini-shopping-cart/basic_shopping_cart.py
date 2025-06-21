cart = [];

while True:
    print("\n==== Welcome to the Shopping Cart🛒 ==== ");
    print("1. View Cart Items📋: ");
    print("2. Add Item🥓: ");
    print("3. Remove Item🗑️: ");
    print("4. Exit Cart ❌:");

    choice = input("\nPlease choose an option below📝: ");

    if choice == "1":
        for item in cart:
            print(f"Your cart currently has: {cart}");
    elif choice == "2":
        item = input("Enter the item: ");
        if item in cart:
            print(f"🚫{item} already in Cart: ");
        else:
            cart.append(item);
            print(f"\n{item} has been added to your cart")
    elif choice == "3":
        item = input("Enter the item to remove: ");
        if item not in cart:
            print(f"{item} does not exist in cart: ");
        else:
            cart.remove(item);
            print(f"{item} has been removed from the cart");
    elif choice == "4":
        print("Thank you for shopping🛍️")
        break
    else:
        print(f"{choice} is not a valid choice!!");

