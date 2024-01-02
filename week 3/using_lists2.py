states = ["Washington", "Oregon", "California"]
states2 = ['Arizona', 'Ohio', 'Louisiana']  # We can concatenate two lists together with the addition operator (+).
best_states = states + states2
# for x in states:
  #  print(x)     #This will print out the above states

# for state in states:
    # print(state)  #Same concept but we are giving x a  descriptive name other than X

# for state in states: # Here we are adding a for loop instead of printing each item
  #  state = state.lower() # This is listing each state again but we are now having them be lowercase
   # print(state)

# print("Washington" in states)  # The "in" keyword can be used on its own, without a for loop 
# print("Tennessee" in states)  # You can use it to construct a conditional expression that evaluates as Boolean True or False
# print("Washington" not in states) # You can also use the not Boolean operator along with it, to flip its return value from True to False or vice versa
  
print(best_states) # Running this will combime both lists as a single one

print(best_states[1:3]) # The following print statements here is using slicing method
print(best_states[:2])
print(best_states[4:])