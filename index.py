import random

# Set the low and high numbers for the range
low = 1
high = 50

# Generate a random number between low and high
correct_answer = random.randrange(low, high)

# Set the number of chances to 5
chances = 5

# Print a welcome message and ask the user to guess a number
print(f"Welcome to the number guesser game! You have {chances} chances to guess a number between {low} and {high}. Good luck!")

while chances > 0:
    # Ask the user to input a number
    user_answer = int(input("Enter your guess: "))

    # Check if the user answer is equal to the correct answer
    if user_answer == correct_answer:
        print("Congratulations! You win!")
        break
    
    # Check if the user answer is smaller than the correct answer
    elif user_answer < correct_answer:
        print("Correct answer is greater!")
        chances -= 1
        
    # Check if the user answer is greater than the correct answer
    elif user_answer > correct_answer:
        print("Correct answer is smaller!")
        chances -= 1

    # Print how many chances are left
    print(f"You have {chances} chances left.")

    # the chances are zero, print a losing message and show the correct answer
    if chances == 0:
        print(f"You lose! The correct answer was {correct_answer}.")
