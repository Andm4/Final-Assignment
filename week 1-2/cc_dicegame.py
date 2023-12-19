import random

high_score = 0

def dice_game():
    global high_score  # To access the global high_score variable

    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2

    print("\nYou roll a... ", dice_1)
    print("You roll a... ", dice_2)
    print("\nYou have rolled a total of: ", total)

    if total > high_score:
        high_score = total
        print("New High Score: ", high_score)

while True:
    print("Current High Score: ", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice: ")

    if choice == "1":
        dice_game()
    elif choice == "2":
        break
    else:
        print("Invalid choice. Please try again.")
   
