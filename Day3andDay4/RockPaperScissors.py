
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Lets start the rock, paper,scissior game")
user_input = input("Type '0' for rock, '1' for paper, and anything for scissior !")
if user_input=='0':
    print(rock)
    print("rock")
elif user_input == '1':
    print(paper)
    print("paper")
else:
    user_input = '2'
    print(scissors)
    print("Scissor")

print("Your Choice: ")
system_input = str(random.randint(0,2))
if system_input=='0':
    print(rock)
    print("rock")
elif system_input == '1':
    print(paper)
    print("paper")
else:
    system_input = '2'
    print(scissors)
    print("Scissor")

print("System Choice: \n")


if user_input == system_input:
    print("match tie!!!")
elif user_input=='0' and system_input=='2':
    print("You win")
elif user_input == '1'and system_input =='0':
    print("You win")
elif user_input == '2' and system_input == '1':
    print("You win")
else:
    print("You Lose") 