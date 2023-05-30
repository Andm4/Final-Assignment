import random

high_score = 0
dice_1 = random.randint(1, 6)
dice_2 = random.randint(1, 6)


def dice_game():

    dice_game()


while True:
    print("Current High Score: ", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
    choice = input("Enter your choice: ")

    if choice == ("1"):
        print("You roll a... ", dice_1)
        print("You roll a... ", dice_2)
        break
