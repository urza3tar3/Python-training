import random
guess = random.randint(1, 10)
guess_counts = 0
while guess_counts < 3:
    guess_counts += 1
    numoftry_left = 3 - guess_counts
    user_guess = input("Guess a number between 1 and 10:")
    if user_guess == guess:
        print("correct answer!")
        break
    else:
        print(f"try again, left {numoftry_left} guesses")
print(f"sorry you ran out of guesses, the number was {guess}")