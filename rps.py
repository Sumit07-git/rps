# Rock Paper and Scissor game which is created using python programming.In this game user has a choice to select from three options.
#if he want to select rock then user has to type rock or if paper then type paper or if scissor then type scissor.Then computer will choose randomPppp option.
# If user wins then user get 1 point or if computer wins then computer get 1 point.
#this program also shows score of both user and computer.

import random

user_score=0
computer_score=0

while True:
  option= ["Rock", "Paper", "Scissor"]
  user_choice= str(input("Enter your choice(Rock , Paper , Scissor):"))
  computer_choice=random.choice(option)

  if user_choice == "Rock" and computer_choice == "Scissor":
    print("You win!")
    user_score+=1

  elif user_choice == "Scissor" and computer_choice == "Paper":
    print("You win!")
    user_score+=1

  elif user_choice == "Paper" and computer_choice == "Rock":
    print("You win!")
    user_score+=1
    
  elif user_choice == computer_choice:
    print("It's a tie!")
  else:
    print("You lose!")
    computer_score+= 1

  print("Your score:",user_score)
  print("Computer score:",computer_score)

  play_again = input(("Do you want to play again? (yes/no): "))
  if play_again.lower() != "yes":
    break