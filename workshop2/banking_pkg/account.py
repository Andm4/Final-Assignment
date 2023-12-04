# adding a function named balance
def show_balance(balance):
    print(f"Your account balance is: ${balance: .2f}")

# Adding the function for deposit
def deposit(balance):
    amount = float(input("Enter amount for deposit"))    

# Adding the function for withdraw
def withdraw(balance):
    amount = float(input("Enter amount to withdraw"))
    return balance - amount