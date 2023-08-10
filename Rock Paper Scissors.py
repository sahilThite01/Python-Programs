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
import random

u_choice = int(input("Choose:\n1 for rock\n2 for paper\n3 for Scissors  "))

image = [rock, paper, scissors]

if u_choice > 3 or u_choice < 0:
    print("\nInvalid input, you lose!")
else:
    print(f"\nYou chose:")
    print(image[u_choice-1])
    
    comp_choice = random.randint(1,3)


    print(f"\nComputer chose:")
    print(image[comp_choice-1])

    rock = 1
    paper = 2
    scissors = 3

    if u_choice == 1 and comp_choice == 2:
        print("You lose")
    elif u_choice == 1 and comp_choice == 3:
        print("You win")
    elif u_choice == 2 and comp_choice == 3:
        print("You lose")
    elif u_choice == 2 and comp_choice == 1:
        print("You win")
    elif u_choice == 3 and comp_choice == 1:
        print("You lose")
    elif u_choice == 3 and comp_choice == 2:
        print("You win")
    else:
        print("It's a tie")

