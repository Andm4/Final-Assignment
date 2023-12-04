from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

#Task 2 registration
print("          === Automated Teller Machine ===          ")
name = input("Enter name to register: ")  #declared a name input
pin = input("Enter PIN: ") # Declared a pin input
balance = "$0" # Balance Variable
print(name, "has been registered with a starting balance of", balance)

# Task 3 Log in and prompt for menu options
print("          === Automated Teller Machine ===          ")
print("LOGIN")

while True:  # Infinite while loop
    name_to_validate = input("Enter name to Login: ") # New variable to store name input
    pin_to_validate = input("Enter PIN: ") # New variable for storing PIN input
    if name_to_validate == name and pin_to_validate == pin: # If statement, AND operator to check if both conditions are true
        print("Login successful!")
        break  # break out of loop if TRUE
    else:  # Print if False, restart loop.
        print("invalid credentials")

# Task 3 second while loop
user = atm_menu(name) #dec variable named User with atm argument

while True:  # 2nd While loop after entering Login
    print(user) # This will print the above argument
    option = input("Choose an option: ") # Added option input for menu

