import random
total_score=0

while True:
    print("Welcome to number guessing game!")
    level=input("Choose difficulty level (easy/medium/hard):").lower()

    if level=="easy":
        max_num=50
        max_attempts=10
    elif level=="medium":
        max_num=100
        max_attempts=7
    elif level=="hard":
        max_num=100
        max_attempts=5
    else:
        print("Invalid input,The program set the difficulty level to medium.")
        max_num=100
        max_attempts=7

    print(f"\nI have selected a number between 1 and 100")
    print(f"You have only {max_attempts} attempts,Try to guess it !!")


    number = random.randint(1,max_num)
    tries=0

    while tries < max_attempts:
        guess=(int(input("Enter your guessing number:")))
        tries+=1
        if guess > number:
            print("Too high! try again Buddy")

        elif guess<number:
            print("Too low! try again Buddy")

        else:
            score=(max_attempts-tries)*10
            total_score += score
            print(f"🥳Correct! You guessed it in {tries}attempts.")
            print(f"Your total_score is:{total_score}")
            break
    else:
        print(f"Game over! You used your all {max_attempts} attempts.")
        print(f"Your total score is :{total_score}")

    play_again =input("Do you want to play Again (yes/no):").lower()

    if play_again!="yes":
        print(f"Thanks for Playing! Final Score:{total_score}")
        print(f"The guessable number is:{number}")
        break