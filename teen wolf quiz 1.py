print("               🐺 ⭐[ 𝐓𝐄𝐄𝐍 𝐖𝐎𝐋𝐅 ]⭐ 🐺               ")
print("")

name = input("please enter your name :  ")
age = input("please enter your age :  ")
print("")
welcoming = input(f"hello {name} welcome to the quiz , are your ready to play ?? \n ")
print("")


question_1 = input(" question 1 : who was the canima ?  \n [ stiles - parish - jackson ] : \n") 




if question_1.lower() == "jackson" : 
  print("")
  print("correct ⭐!")
  print("")
  question_2 = input("question 2 : what is the name of lydia's dog ? \n [ lily - prada - luna] : \n")

  

  if question_2.lower() == "prada":
    print("")
    print("correct⭐!")
    print("")
    question_3 = input("question 3 : who is the benefactor ? \n  [ jerrard - kate - meredeth ] : \n ")


    
    if question_3.lower()  == "meredeth":
      print("")
      print(" correct⭐! you have completed the quiz \n \n your score is : 3/3")
      
    else :
      print("")
      print("incorrect , the answer is meredeth")
      print("your score is : 2/3")

    
  
  else :
    print("incorrect , the answer is prada \n please try again ")

  

else:
  print("incorrect , the answer is jackson \n your score is 0/3")
