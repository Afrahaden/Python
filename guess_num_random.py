import random
secret_num = random.randint(1, 10)
guess = None
count = 3
while True:
    if guess != secret_num:
        guess = int(input(f"You have {count} attempts. Guess the secret number from 1 to 10: "))
        count -= 1

        if count == 0:
            print("\nGame over!!!")
            break
        if guess > secret_num:
            print(f"Sorry, try again. Too high. You have {count} attempts left. \n")
        elif guess < secret_num:
            print(f"Sorry, try again. Too low. You have {count} attempts left. \n")
    else:
        print(f"\nCongrats, you have guessed {secret_num} correctly!!")
        break





# import random
#
#
# def guess_num(x):
#     random_num = random.randint(1, x)
#     guess = 0
#     while guess != random_num:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_num:
#             print("Sorry, guess again. Too low.\n")
#         elif guess > random_num:
#             print("Sorry, guess again. Too high.\n")
#
#     print(f"\nCongrats. You have guessed the number {random_num} correctly!!")
#
#
# guess_num(50)
