
#library
library = []
book_own = input("Enter the name of a book you own : ")
library.append(book_own)
another_book_own = input("""
Enter the name of another book you own (or press 'ENTER' to skip) : 
""")
if another_book_own :
  library.append(another_book_own)
  print(f"your library : {library}")
  print("")

else :
  print(f"your library : {library}")
  print("")


#wishlist
wishlist = []
book_wish = input("""
Enter the name of a book you wish to have in the future : 
""")
wishlist.append(book_wish)
another_book_wish = input("""
Enter the name of another book you wish to have (or press 'ENTER' to skip) :
""")
if another_book_wish :
  wishlist.append(another_book_wish)
  print(f"your wishlist : {wishlist}")
  print("")

else :
  print(f"your wishlist : {wishlist}")
  print("")
#aquired
aquired = input("""
Enter a name from your wishlist that you've aquired (or press 'Enter' to skip :
""")
if aquired in wishlist :
  library.append(aquired)
  wishlist.remove(aquired)
  print(f"upadated library : {library}")
  print(f"updated wishlist : {wishlist}")
  print("")
else :
  print(f"your library : {library}")
  print(f"your wishlist : {wishlist}")
  print("")
#donated
donated = input("""
Enter the name of a book from your library you donated (or press 'Enter' to skip : 
""")
if donated in library :
  library.remove(donated)
  print(f"final library after donations : {library}")

else : 
  print(f"your library : {library}")