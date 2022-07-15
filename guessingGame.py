# simple iteration

key = 8
guess = 0
count = 0

while guess != key and count < 5:
    if count > 0:
        print("Wrong, guess again,", count, "guesses used")
    guess = int(input("Guess a number 1-10: "))
    count += 1

if count == 5:
    print('You lose!')

if guess == key:
    print("Winner winner chicken dinner")


