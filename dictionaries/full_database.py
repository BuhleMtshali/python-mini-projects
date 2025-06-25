import json

# Initialize empty user list
users = []

# === Function to check for duplicate names ===
def is_duplicate(name):
    for user in users:
        if user['name'].lower() == name.lower():
            return True
    return False

# === Function to count roles ===
def count_roles():
    admin_count = 0
    user_count = 0
    for u in users:
        if u['role'].lower() == "admin":
            admin_count += 1
        elif u['role'].lower() == "user":
            user_count += 1
    return admin_count, user_count

# === Function to view all users ===
def view_users():
    if not users:
        print("🚫 No users found.")
        return
    print("\n=== 👥 All Users ===")
    for user in users:
        print(f"- {user['name']} ({user['age']}), from {user['city']}, role: {user['role']}")
    print()

# === Function to filter by city ===
def filter_by_city():
    city = input("Enter city to filter by: ").lower()
    found = False
    print(f"\nUsers from {city.title()}:")
    for user in users:
        if user['city'].lower() == city:
            print(f"- {user['name']} ({user['age']}) – {user['role']}")
            found = True
    if not found:
        print("🚫 No users found in that city.")

# === Function to save users to file ===
def save_to_file():
    with open("users.json", "w") as f:
        json.dump(users, f, indent=4)
    print("✅ Users saved to 'users.json' file.")

# === MAIN PROGRAM LOOP ===
while True:
    print("\n=== 🛠️ User Management Menu ===")
    print("1. Add New User")
    print("2. View All Users")
    print("3. Filter Users by City")
    print("4. Count Admins vs Users")
    print("5. Save to File")
    print("6. Exit")

    choice = input("Pick an option (1-6): ")

    if choice == "1":
        print("\n-- Add New User --")
        name = input("Enter name: ")
        if is_duplicate(name):
            print("🚫 That name already exists! Try a different one.")
            continue
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("❌ Invalid age! Must be a number.")
            continue
        city = input("Enter city: ")
        role = input("Enter role (admin/user): ").lower()
        if role not in ["admin", "user"]:
            print("❌ Invalid role! Must be 'admin' or 'user'.")
            continue

        user = {
            "name": name,
            "age": age,
            "city": city,
            "role": role
        }
        users.append(user)
        print(f"✅ {name} has been added.")

    elif choice == "2":
        view_users()

    elif choice == "3":
        filter_by_city()

    elif choice == "4":
        admin_count, user_count = count_roles()
        print(f"\n🔢 Admins: {admin_count}, Users: {user_count}")

    elif choice == "5":
        save_to_file()

    elif choice == "6":
        print("👋 Bye bestie! Exiting the app.")
        break

    else:
        print("❌ Invalid option. Please choose 1–6.")
