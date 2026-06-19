import random
def play_game():
    print("\n Number Guessing name")
    print("\n select difficulty level:")
    print("1. easy(10 attempts)")
    print("2 Medium (7 attempts)")
    print("3.Hard(5 attemps)")
    
    choice=input("enter your choice(1/2/3):")
    
    if choice=="1":
        attempts=10
    elif choice=="2":
        attempts=7
    elif choice=="3":
        attempts=5
    else:
        print("invalid choice! defaulting to easy mode")
        attempts=10
        
    secret_number=random.randint(1,100)
    print("\n I have selected a number between 1 and 100")
    print(f"you have{attempts} attempts to guess it.")
    
    while attempts >0:
        try:
            guess=int(input("enter your guess:"))
            if guess<1 or guess >100:
                print("please enter a number between 1 and 100.")
                continue
            if guess ==secret_number:
                print("\n congratulations!")
                print("you guessed the correct number!")
                return
            elif guess <secret_number:
                print("too low!")
            else:
                print("too high!")
                
            attempts -=1
            print(f"remaining attempts:{attempts}")
            
        except ValueError:
            print("invalid input! please enter a number.")
    print("\n game over!")
    print(f"the coorect number was:{secret_number}")
print("welcome to number guessing game")
while True:
    play_game()
    again=input("\n do you want to play agin>(yes/no): ").lower()
    if again !="yes":
        print("\n thank you for playing")
        break
