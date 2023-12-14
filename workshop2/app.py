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
user_data = {name: {"pin": pin, "balance": 0}} # Balance Variable
print(f"{name} has been registered with a starting balance of ${user_data[name]['balance']}")

# Task 3 Log in and prompt for menu options
print("          === Automated Teller Machine ===          ")
print("LOGIN")

while True:  # Infinite while loop
    name_to_validate = input("Enter name to Login: ") # New variable to store name input
    pin_to_validate = input("Enter PIN: ") # New variable for storing PIN input
    if name_to_validate in user_data and pin_to_validate == user_data[name_to_validate]["pin"]: # If statement, AND operator to check if both conditions are true
        print("Login successful!")
        break  # break out of loop if TRUE
    else:  # Print if False, restart loop.
        print("invalid credentials")
user_balance = user_data[name]["balance"]


while True:  # 2nd While loop after entering Login
    user = atm_menu(name)
    option = input("Choose an option: ") # Added option input for menu
    if option == "1" or option.lower() == "balance":
        account.show_balance(user_balance)
    elif option == "2" or option.lower() == "deposit":
        user_balance = account.deposit(user_balance)
        account.show_balance(user_balance)
    elif option == "3" or option.lower() == "withdraw":
        user_balance = account.withdraw(user_balance)
        account.show_balance(user_balance)
    elif option == "4" or option.lower() == "logout":
        account.logout(name)
        break
