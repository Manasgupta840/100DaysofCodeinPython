word_list = ["camel","baloon","shark"]
import random
chosen_word = random.choice(word_list)
guess = input("Geuss a letter: ").lower()
for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")




word_list = ["camel","baloon","shark"]
import random
chosen_word = random.choice(word_list)
display = []
for _ in range(len(chosen_word)):
  display += "_"
print(display)

while("_" in display):
  guess = input("Geuss a letter: ").lower()
  for i in range(len(chosen_word)):
    if(chosen_word[i] == guess):
      display[i] = guess
  print(display)

