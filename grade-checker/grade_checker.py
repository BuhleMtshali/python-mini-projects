user_name = input("Enter your name👩🏼‍🎓: ");
user_subject = input("Enter Subject📚: ");
user_grade = int(input("Enter your Grade🧮: "));
pass_mark = 50;

if user_grade < 50:
    print(f"Unfortunately {user_name} you have have received {user_grade}%, which is below the {pass_mark}% pass mark🥺");
elif user_grade == 50:
    print(f"Whew!! {user_name}, your current grade is {user_grade}% which is right on the dot of the {pass_mark}% pass mark😮‍💨");
elif user_grade <= 75:
    print(f"{user_name}, congrats on your {user_grade}% mark, which is way above the {pass_mark}% pass mark👏");
else:
    print(f"Huzzah!! {user_name}! you've bagged yourself a Distinction!!!!")