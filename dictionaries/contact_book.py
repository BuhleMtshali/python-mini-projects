#first define the list that will hold the added numbers
contact_book = [];

#print the welcome message
welcome_message = "===== 👋🏻Welcome to you own Personalized Contact Book📲 =====";
menu_message = "\n==== Contact Book Menu🔢 ===="
print(welcome_message)

#get the user's details
user_name = input("Enter your name👥: ");
user_lastname = input("Enter your last nameℹ️: ");

#Validating the user's phone number with a while loop
while True:
    user_number = input("Enter your 10-digit phone number📲: ")
    if user_number.isdigit() and len(user_number) == 10:
        break;
    else:
        print("❌ Please enter exactly 10 digits - numbers only!")


#validate the email with a while loop
while True:
    user_email = input("Enter your email📧: ")
    if "@" in user_email and "." in user_email:
        break
    print("Invalid email format🚫")

#show the user's info
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

#start the loop for the contact book
while True:
    print(menu_message)
    print("1. Add Contact👤: ")
    print("2. View Contact List👥: ")
    print("3. Delete Contact🗑️: ")
    print("4. Exit❌")

    #getting the user's response
    choice = input(f"\n{user_name}, please choose an option to continue")

    #creating if statements for the different options
    if choice == "1":
        while True:
            new_contact_name = input("Enter New Contact's Name: ");
            new_contact_lastname = input("Enter New Contacts Last Name: ")

            #validate the new user's number
            while True:
                new_contact_number = input("Enter New Contacts Number: ")
                if new_contact_number.isdigit() and len(new_contact_number) == 10:
                    break
                else:
                    print(f"{new_contact_name}'s phone number format is incorrect, please try again🚫")
            
            #creating the new contact dictionary
            new_contact = {
                "new_contact_name": new_contact_name,
                "new_contact_lastname": new_contact_lastname,
                "new_contact_number": new_contact_number
            }

            #append the dictionary to the list
            contact_book.append(new_contact);
            print(f"✅ {new_contact_name} has been successfully added to your contact list!!!")

            #ask if the user wants to add more people or break the loop
            add_more = input("Do you want to add another contact (yes/no): ")
            if add_more != "yes":
                break

    elif choice == "2":
        #if contact book is currently empty
        if not contact_book:
            print(f"{user_name}, your contact book is currently empty. Lets add people first!!")
        else:
            print(f"\n ----{user_name} here is your contact listℹ️ ----")

            for contact in contact_book:
                print(f"""
==== Contact Infor👾 ====
Name: {contact["new_contact_name"]}
Last Name: {contact["new_contact_lastname"]}
Phone number: {contact["new_contact_number"]}
==================================
                  """)
                
    elif choice == "3":
        if not contact_book:
            print("Your Contact Book is currently empty, there's nothing to remove!!!")
        else:
            remove_contact = input("Enter the name of the contact you want to remove: ")
            for contact in contact_book:
                if remove_contact.lower() == contact["new_contact_name"].lower():
                    contact_book.remove(contact)
                    print(f"✅ {remove_contact} was successfully removed from contact book")
                    break
                else:
                    print(f"🚫 {remove_contact} does not exist in inventory")

    elif choice == "4":
        print(f"👋🏻 Thank you for using Mini Contact Book, {user_name}")
        break

    else:
        print("❌Invalid choice, please choose 1-4")