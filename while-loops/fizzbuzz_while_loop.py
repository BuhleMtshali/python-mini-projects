#example of while loop
number = 1

while number <= 20:
    if number % 3 == 0 and number % 5 == 0:
        print('Double fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
    number += 1