import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    choice = input("Press enter to pick a card, or Q then enter to quit: ") #prompting the user to make a choice witht he input function   
    if choice == "":
        picked_card = random.choice(diamonds) # This line checks if the user pressed enter (an empty string) if the condition is true. executes this block
        print("your hand: ", [picked_card]) #loop moves to this line and uses random.cboice method to randomly select a card from the list
        hand.append(picked_card) # this line prints the selected card to the consolem indicating that is is now part of the users hand
        diamonds.remove(picked_card) # this line then adds the selected card to the "hand" list
        print("remaining cards: ", diamonds) # this line tells loop to print the remaining cards in list
    if not diamonds: # This if statement if true will print the string below when no cards are left
        print("There are no more cards to pick")
    elif choice == "Q": #exits the loop
        break