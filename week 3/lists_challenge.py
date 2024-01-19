import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Press enter to pick a card, or Q then enter to quit: ") #prompting the user to make a choice witht he input function   
    if choice == " ":
        print("your hand: ", random.choices(diamonds))
    if choice == "Q":
        break