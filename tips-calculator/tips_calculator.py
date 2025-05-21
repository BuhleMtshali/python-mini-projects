import math

order_total = float(input("Enter your Order Total🍱: "));
people = int(input("How many people are you splitting the amount with👭: "));
tip_percentage = float(input("What percentage is your tip💰: "));
tip_amount = tip_percentage / 100;
total_amount = order_total + tip_amount;
amount_per_person = total_amount / people;

print("----Order Receipt🔖----");
print("----Order Summary🍱----");
print(f"Order Total: R{order_total}");
print(f"People Dining: {people}");
print(f"Tip Percentage: {tip_percentage}%");
print(f"Total Amount(with tip): R{total_amount}");
print(f"Amount Per Person: R{round(amount_per_person), 2}");
print("-----Thank You----");