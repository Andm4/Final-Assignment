states = ["Washington", "Oregon", "California"]
# for x in states:
  #  print(x)     #This will print out the above states

# for state in states:
    # print(state)  #Same concept but we are giving x a  descriptive name other than X

for state in states: # Here we are adding a for loop instead of printing each item
    state = state.lower() # This is listing each state again but we are now having them be lowercase
    print(state)