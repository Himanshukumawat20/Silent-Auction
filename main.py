from replit import clear
from art import logo
print(logo)
bidding = True
bider = {}
def find_highest_bidder():
  highest_bid = 0
  highest_bidder = ""
  for bids in bider:
    if bider[bids] > highest_bid:
      highest_bid = bider[bids]
      highest_bidder = bids
  print(f"Highest bider is {highest_bidder} with the bid of ${highest_bid}")

while bidding:
  name = input("What is your name? \n")
  bid = int(input("What is your bid? \n$"))
  new_bider = input("Want to add new bider? type 'yes' or 'no' \n")
  bider[name] = bid
  if new_bider == "yes":
    clear()
    print(logo)
  elif new_bider == "no":
    bidding = False
    find_highest_bidder()
    
