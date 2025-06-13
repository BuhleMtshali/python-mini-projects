guests = ["kate", "linda", "robert", "kim", "tonya", "zack", "ed", "mike"] #this is the list of peopl i will be inviting\

#addign more people to the list
guests.insert(0, "meg");
guests.insert(5, "todd");
guests.append("zendaya")

#sorting the list in alpahbetical order
guests.sort();
print(f"Sorted list: {guests}");

#sorting the list in reverse
guests.sort(reverse=True);
print(f"Reversed string: {guests}");

#I will use a loop to send each of them an invite
for guest in guests:
    if guest == "ed":
        print(f"Thank for your RSVP {guest}, its a shame you wont be thre!");
    else:
        print(f"Good day {guest.title()}, I would like to formally invite you to my current event taking place tomorrow!");