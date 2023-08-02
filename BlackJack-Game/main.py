
import random
from replit import clear
from art import logo
print(logo)
name = input("What is your name? ")
game_is_over = False
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def calculate_scores(list):
  """It calculate the scores of given list"""
  if sum(list)==21 and len(list)==2:
    return 0
  if 11 in list and sum(list)>21:
    list.remove(11)
    list.append(1)
  return sum(list)
def compare(user_score,computer_score):
  """It compares the scores of user and computer"""
  if user_score==computer_score:
    return "Its a draw!"
  elif computer_score==0:
    return "lose,opponent has a blackjack"
  elif user_score==0:
    return "Hurray! Win the game with blackjack!"
  elif user_score>21:
    return "You went over 21,you lose!!"
  elif computer_score>21:
    return "You win "
  elif user_score>computer_score:
    return "You win"
  else:
    return "Alas!,You lose!"

def play_game():
  """This plays the game of Blackjack"""
  user_cards = []
  computer_cards = []
  for card in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_is_over:
    user_score=calculate_scores(user_cards)
    computer_score=calculate_scores(computer_cards)
    
    print(f"{name} has cards {user_cards} has score of {user_score}")
    print(f"computer hai card {computer_cards[0]} and 1 hidden card")
    
    if user_score==0 or computer_score==0 or user_score>21:
      game_is_over = True
    else:
      user_deal = input("Type y to get another card or type n to pass").lower()
      if user_deal=="y":
        user_cards.append(deal_card())
      else:
        game_is_over=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score = calculate_scores(computer_cards)
  
  print(f"Your final hand {user_cards} and final score: {user_score}")
  print(f"Computer final hand {computer_cards} and final score: {computer_score}")
  print(compare(user_score,computer_score))

while input("Do you want to play game of BlackJack! type y for yes and n for no: ").lower() == "y":
  clear()
  play_game()