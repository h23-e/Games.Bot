print("welcome to place the rabbit \n")
field = [["🌿","🌿","🌿"],["🌿","🌿","🌿"],["🌿","🌿","🌿"]]

print(f"{field[0]}\n{field[1]}\n{field[2]}")
print("where should the rabbit go ? 🐇 ")

position = (input("please choose a row and a column : "))
#الرو حق الرقم الاول الي على اليسار والكولمن حق الثاني الي على اليمين 23 نبي نسيفهم و نحولهم ارقام 
int_row = int(position[0])
int_column = int(position[1])

#عشان اعادل بين عد الكمبيوتر الي من صفر وعد المستخدم الي من واحد اطرح من واحد  
field[int_row - 1][int_column - 1] = "🐇"

print("\n success ....\n")
print(f"{field[0]}\n{field[1]}\n{field[2]}")