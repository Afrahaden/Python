secret_number = 5
guess_count = 0
guess_limit = 3
print('Guess a secret the number between 1 to 10')
print(f"You have {guess_limit} attempts to guess the secret number.")

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('\nCongrats! you have won!')
        break
    elif guess < secret_number:
        print("\nToo low\n")
    elif guess > secret_number:
        print("\nToo high\n")
else:
    print("Sorry, you failed!")
