# Display the art

from art import logo, vs
from game_data import data
import random
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
  def format_data(account):
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"
  
  def check_answer(guess, follower_a, folower_b):
    if follower_a > follower_b:
      return guess == "a"
    else:
      return guess == "b"
  
  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
  
  print(f"compare A: {format_data(account_a)} ")
  
  print(vs)
  
  print(f"Against  B : {format_data(account_b)}")
  
  guess = input("Who has more follower 'A' or 'B' : ").lower()
  follower_a = account_a["follower_count"]
  follower_b = account_b["follower_count"]
  
  is_correct = check_answer(guess,follower_a, follower_b )
  
  if is_correct:
    score += 1
    print(f"You are right ! curreent score {score}")
  else:
    print(f"You are wrong ! Final score {score}")
    game_should_continue = False
    