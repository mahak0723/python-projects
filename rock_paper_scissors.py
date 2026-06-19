import random

choices = ["rock", "paper", "scissor"]
computer = random.choice(choices)

user = input("Enter rock, paper or scissor: ").lower()

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")

elif ((user == "rock" and computer == "scissor") or
      (user == "paper" and computer == "rock") or
      (user == "scissor" and computer == "paper")):
    print("You win!")

else:
    print("Computer wins!")
