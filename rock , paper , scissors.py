#عشان اخلي الكمبيوتر يختار عشوائي
import random

#--------------------------------------------------------------------------------

#one : save acsii in variables
rock_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper_ascii ="""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#--------------------------------------------------------------------------------

#two : welcoming + rules

print("👊✋✌️ welcome to the rock , paper , scissors game 👊✋✌️  ")
confirm = input("press enter to continue or type (help) for the rules : ")

if confirm.lower() == "help" :
  print("""
        **********      ⛔RULES⛔     *********
        1) you choose and the computer chooses
        2) rock smashes scissors -> rock wins
        3) scissors cut paper -> scissors wins 
        4) papers covers rock -> paper wins
  """)

#--------------------------------------------------------------------------------
  
#three : log the user answer + if invalid print invalid choice
user_choice = input("Enter your choice (rock , paper , scissors): ").lower()
if user_choice not in ["rock" , "paper" , "scissors"] :
  print("")

#--------------------------------------------------------------------------------

#four : if valid display user choice in ascii 
elif user_choice == "rock" : 
  print(f"you chose : \n{rock_ascii}")

elif user_choice == "paper" : 
  print(f"you chose : \n{paper_ascii}")

elif user_choice == "scissors" :
  print(f"you chose : \n{scissors_ascii}")

#----------------------------------------------------------------------------------

#five : computer choice 
computer_choice = random.choice(["rock" , "paper" , "scissors"])
if user_choice not in ["rock" , "paper" , "scissors"] :
  print("invalid choice , please try again ..")

elif computer_choice == "rock" : 
  print(f"computer chose : \n{rock_ascii}")

elif computer_choice == "paper" : 
  print(f"computer chose : \n{paper_ascii}")

elif computer_choice == "scissors" :
  print(f"computer chose : \n{scissors_ascii}")



#----------------------------------------------------------------------------------

#six : who wins?
#invalid choice 
if user_choice not in ["rock" , "paper" , "scissors"] :
  print("")

#سيناريو التعادل
elif user_choice == computer_choice :
  print("its a tie")



## سيناريو الفوز
elif (
  (user_choice == "rock" and computer_choice == "scissors") 
  or
  (user_choice == "paper" and computer_choice == "rock")
  or 
  (user_choice == "scissors" and computer_choice == "paper")
) : 
  print(f"you win ! {user_choice} beats {computer_choice}")

##سيناريو الخساره
else :
  print(f"you lose ! {computer_choice} beats {user_choice}")