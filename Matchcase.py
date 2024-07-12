#Guess game uisng Match case
import random
secret_number = random.randint(1, 3)
guess = int(input("I am thinking of a number between 1 and 5 can you guess it: "))
while true:
    match guess:
        case 1:
            if secret_number == 1:
                print("Congratulations you guessed the number correctly")
            else:
                print("Nope, your guess is a little low, try again")
        case 2:
            if secret_number == 2:
                print("Congratulations you guessed the number correctly")
            elif secret_number < 2:
                print("Oops your guess is a liitle bit high, can you guess again")
            else:
                print("Nope, your guess is a little bit low try again")
        case 3:
            if secret_number == 3:
                print("Congratulations you guessed the number correctly")
            elif secret_number < 3:
                print("Oops your guess is a liitle bit high, can you guess again")
            else:
                print("Nope, your guess is a little bit low try again")
        case _:
            print("Enter a valid number between 1 and 3")

