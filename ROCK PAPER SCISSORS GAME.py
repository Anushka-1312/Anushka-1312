#!/usr/bin/env python
# coding: utf-8

# # PROJECT-5 ESSENTIALS OF PYTHON PROGRAMMING

# Aim: Write a Python program to develop a Rock, Papers and Scissors game to be played against a computer.

# IDE USED:JUPYTER NOTEBOOK
# 

# In[1]:


import random


# SOURCE FOR ASCII ART:https://ascii.co.uk/art

# In[2]:


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


# In[3]:


paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''


# In[4]:


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# RULES
# 
# THERE ARE THREE RULES FOR PLAYING ROCK,PAPER,SCISSORS GAME
# 
# 1.ROCK CRUSHES SCISSORS
# 
# 2.SCISSORS CUTS PAPER
# 
# 3.PAPER COVERS ROCK

# In[5]:


game_images = [rock, paper, scissors]


# In[6]:


while(True):
#Prompting the user to choose any one of the inputs i.e Rock,Paper,Scissors
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
#Main logic of the program
    if user_choice >= 3 or user_choice < 0: 
        print("You typed an invalid number, you lose!") 
    else:
        print(game_images[user_choice])

        computer_choice = random.randint(0, 2)
        print("Computer chose:")
        print(game_images[computer_choice])


        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")
            
###Prompting the user aking if he/she wants to play again
        play_again=str(input("Do you want to play again?type y for yes and Q for no"))
        if(play_again!='y'):
            break


# In[ ]:




