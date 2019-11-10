import random
my_random_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
no_win = True

while no_win:
    user_number = int(input("What's the number? "))
    if user_number > my_random_number:
        print(user_number, " is too high.")
    elif user_number == my_random_number:
        print("Winner!")
        no_win = False
    else:
        print(user_number, " is too high.")