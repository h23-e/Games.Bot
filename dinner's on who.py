import random
names = input("""

 __| |____________________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
   | |                                            | |
   | |                                            | |
   | |   Welcome to * 🍽️ DINNER's ON WHO 🍽️ *    | |
   | |     you  will give me a list of names      | |
   | |         and i will choose who pays ..      | |                           
   | |                                            | |
   | |                                            | |
 __| |haya esmaiel________________________________| |__
(__   ____________________________________________   __)
   | |                                            | |
          

 if you're ready , enter the names seperated by comma : \n """).split(", ")
random_names = random.choice(names)
print(f"dinner is on 🍔🍕🌮 {random_names} 🍔🍕🌮")
input("""



press enter to exit..""")
