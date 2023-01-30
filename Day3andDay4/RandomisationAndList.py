import random

random_side = random.randint(0,1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")

# https://docs.python.org/3/tutorial/datastructures.html

#List
states_of_america = ["Delaware","Maine","Ohio"]
print(states_of_america[0])
print(states_of_america)
print(states_of_america[-2]) #from the last

#change the element
states_of_america[1] = "Delaaware"
print(states_of_america[1])

#Add element in the end of the list
states_of_america.append("Alaska")

print(states_of_america)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


name = random.choice(names)
print(name+" is going to buy the meal today!")