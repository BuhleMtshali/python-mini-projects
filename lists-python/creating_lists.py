dog_lists = ['masey', 'ava', 'maccarooni', 'rex'];

print("===== Welcome To The Dog Park🐶 =====")

dog_name = input("Enter the name of your dog: ");


if dog_name in dog_lists:
    print(f"{dog_name} is already at the park");
else:
    dog_lists.append(dog_name);
    print(f"{dog_name} wasn't at the park but he has just arrived!!!");

        