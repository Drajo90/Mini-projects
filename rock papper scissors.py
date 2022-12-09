import random

def play():
    total_games = 0
    winning_streak = 0
    number_of_games = int(input("How many games would you like to play?\n"))
    list1= ["rock", "papper", "scissors"]
    user_wins = 0
    computer_wins = 0

# Still working on adding the segment of code if there is a wrong user input to give 3 max tries then terminate the loop
    while total_games < number_of_games:
        user = input("What is your choice: rock , papper or scissors?\n").lower()
        computer = random.choice(["rock" ,"papper" ,"scissors" ])

        if user not in list1:
            print("You have not chosed proper tool for fight.")
            continue

        if user == computer:
            total_games += 1
            winning_streak = 0
            print("It is a tie! No one won this time.")

        elif win(user,computer):
            total_games += 1
            winning_streak += 1
            user_wins += 1
            print(f"You have won! CONGRATULATIONS. You are in winning streak of {winning_streak}")
        else:
            print("You have lost. Try again!")
            total_games += 1
            winning_streak = 0
            computer_wins += 1
    print(f"The Game has ended and total games played were {total_games}. \nYour score: {user_wins}\nComputer score: {computer_wins}")

def win(user,computer):
# Returns true if the user has won the game
    if (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "papper") or (user == "papper" and computer == "rock"):
        return True
    
print(play())