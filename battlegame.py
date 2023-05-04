#Task 1
wizard = "Wizard"
elf = "Elf"
human = "Human"
drago ="Dragon"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50

#Task 2 & 3
while True:
    print ("1) Wizard")
    print ("2) Elf")
    print ("3) Human")
    character = input("Choose your character: ")

    if character.lower() in ["1", "wizard"]:
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character.lower() in ["2", "elf"]:
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character.lower() in ["3", "human"]:
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    else:
        print ("Unknown character")

print("You chose the: ", character)
print("Health: ", my_hp)
print("Damage: ", my_damage, "\n")

while True:
    dragon_hp = dragon_hp - my_damage
    my_hp = my_hp - dragon_damage
    print("The", character, "damaged the Dragon!")
    print("The Dragon's hit points are now:", dragon_hp, "\n")

    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break

    print("The Dragon strikes back at", character)
    print("The", character + "'s", "hitpoints are now:", my_hp, "\n")

    if my_hp <= 0:
        print("The", character, "has lost the fight for asgard")
        break