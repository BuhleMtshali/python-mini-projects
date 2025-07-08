# Define the contact book list
contact_book = []

# Welcome message
welcome_message = "===== 👋🏻 Welcome to your Personalized Contact Book📲 ====="
menu_message = "\n==== Contact Book Menu🔢 ===="
print(welcome_message)

# Get user info
user_name = input("Enter your name👥: ")
user_lastname = input("Enter your last nameℹ️: ")

# Validate phone number
while True:
    user_number = input("Enter your 10-digit phone number📲: ")
    if user_number.isdigit() and len(user_number) == 10:
        break
    else:
        print("❌ Please enter exactly 10 digits - numbers only!")

# Validate email
while True:
    user_email = input("Enter your email📧: ")
    if "@" in user_email and "." in user_email:
        break
    print("Invalid email format🚫")

# Show profile
print("✅ User Profile successfully Created👤")
print(f"""
--------------------------
==== User Details👥 ====
Name👤: {user_name}
Last Name🧍🏼: {user_lastname}
Phone Number🔢: {user_number}
User Email📧: {user_email}
----------------------------
""")

# Start app loop
while True:
    print(menu_message)
    print("1. Add Contact👤")
    print("2. View Contact List👥")
    print("3. Delete Contact🗑️")
    print("4. Search Contact🔍")
    print("5. Exit❌")

    choice = input(f"\n{user_name}, please choose an option to continue: ")

    if choice == "1":
        while True:
            name = input("Enter New Contact's Name: ")
            lastname = input("Enter New Contact's Last Name: ")

            while True:
                number = input("Enter New Contact's Number: ")
                if number.isdigit() and len(number) == 10:
                    break
                else:
                    print(f"{name}'s phone number format is incorrect, please try again🚫")

            # Add to contact book
            new_contact = {
                "name": name,
                "lastname": lastname,
                "number": number
            }

            contact_book.append(new_contact)
            print(f"✅ {name} has been successfully added to your contact list!")

            add_more = input("Do you want to add another contact (yes/no): ").lower()
            if add_more != "yes":
                break

    elif choice == "2":
        if not contact_book:
            print(f"{user_name}, your contact book is empty. Let's add someone first!")
        else:
            print(f"\n📓 ---- {user_name}'s Contact List ----")
            for contact in contact_book:
                print(f"""
==== Contact Info 👾 ====
Name: {contact["name"]}
Last Name: {contact["lastname"]}
Phone Number: {contact["number"]}
=========================
""")

    elif choice == "3":
        if not contact_book:
            print("Your Contact Book is currently empty. Nothing to remove!")
        else:
            remove_name = input("Enter the name of the contact you want to remove: ").lower()
            found = False
            for contact in contact_book:
                if remove_name == contact["name"].lower():
                    contact_book.remove(contact)
                    print(f"✅ {remove_name.capitalize()} was removed from the contact book.")
                    found = True
                    break
            if not found:
                print(f"🚫 No contact found with the name {remove_name}.")

    elif choice == "4":
        if not contact_book:
            print("Your Contact Book is empty. Try adding contacts first.")
        else:
            search_name = input("Enter the name of the contact to search for: ").lower()
            found = False
            for contact in contact_book:
                if search_name in contact["name"].lower():
                    print(f"""
==== Contact Found 🔍 ====
Name: {contact["name"]}
Last Name: {contact["lastname"]}
Phone Number: {contact["number"]}
=========================
""")
                    found = True
            if not found:
                print(f"🚫 No contact found with the name {search_name}.")

    elif choice == "5":
        print(f"👋🏻 Thank you for using Mini Contact Book, {user_name}!")
        break

    else:
        print("❌ Invalid choice, please choose between 1 and 5.")
