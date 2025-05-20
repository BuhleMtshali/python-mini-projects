item = input("What Item do you want to order? ");
price = float(input("How much does it cost? "));
quantity = int(input("How many would you like? "));
total = price * quantity;
print(f"You have ordered {quantity} x {item} and your order total is R{total}")