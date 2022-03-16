import random

continue_game = True

# Game images

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
game_images = [rock, paper, scissors]

print("Let's play some rock, paper, scissors!\n")

def play_round():
  continue_game = True
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. Or type 3 to exit\n"))
  if user_choice != 0 and user_choice != 1 and user_choice != 2 and user_choice != 3: 
    print("\nInvalid option.\n") 
  else:
    if user_choice != 3:
      print(game_images[user_choice])
      computer_choice = random.randint(0, 2)
      print("Computer chose:")
      print(game_images[computer_choice])
      if user_choice == 0 and computer_choice == 2:
          print("You win!\n")
      elif computer_choice == 0 and user_choice == 2:
          print("You lose\n")
      elif computer_choice > user_choice:
          print("You lose\n")
      elif user_choice > computer_choice:
          print("You win!\n")
      elif computer_choice == user_choice:
          print("It's a draw\n")
      print("Let's go again!\n")
    else:
      continue_game = False
      print("Good bye!")
  return continue_game

while continue_game:
  continue_game = play_round()