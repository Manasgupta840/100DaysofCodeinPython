logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
initialize = True
bid_dic = {}
max = 0
max_key = ""
while initialize:
  name = input("what is your name?: ")
  bid = int(input("What's your bid?: $"))
  bid_dic[name] = bid
  if bid>max:
    max = bid
    max_key = name
  initialize = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  if(initialize == "yes"):
    initialize = True
  elif(initialize == "no"):
    initialize = False
  else:
      print("You type invalid input !!! ")
      break
print(f"The winner is {max_key} with a bid of ${bid_dic[max_key]}")
