states = ["Washington", "Oregon", "California"]
print(states[0])
print(states[1])
print(states[2])

# print(states[-1]) # This will list the states in reverse
# print(states[-2])
# print(states[-3])

states[2] = "Arizona"
# print(states) # This replaces califorina with Arizona

# print(len(states)) # finding the length of a list

# using List Methods
states.append("New York")
print(states) # The append method adds an item to the end of the list

states.pop()
print(states) # The pop method removes the last item on the list

states.pop(1)
print(states) # same pop method but removes the item based on the index number oregon
          