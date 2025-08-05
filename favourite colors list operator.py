add_color = input("add the first color you like : \n")
colors = []
color_one = colors.append(add_color)
color_two = input("do you want to add more colors? yes or no ? \n")
if color_two.lower() == "yes" : 
  another_color = input("add another color to the list : \n")
  colors.append(another_color)
  print("the colors you like are :")
  print(colors)
else :
  print("the colors you like are :")
  print(colors)