# if condition:
#   do this
# else:
#   do this


# if condition:
#   do this
# elif condition:
#   do this
# else:
#   do this


print("Welcome to the rollerCoaster!")
height = int(input("What is your height in cm? "))

if height>120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

  # if condition:
  #     if anoter condition:
  #         do
  #         this
  #     else:
  #         do
  #         this
  # else:
  #     do
  #     this

print("Welcome to the rollerCoaster!")
height = int(input("What is your height in cm? "))

if height>120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride.")

  
#
# OPERATOR DESCRIPTION SYNTAX
#
# and ==> Logical AND ==>: True if both the operands are true x and y
# or ==> Logical OR ==>: True if either of the operands is true x or y
# not ==> Logical NOT ==>: True if operand is false not x