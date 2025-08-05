import random
#مراحل هانق مان بالاسكي
hangman_stages = [
  """
  +---+
  |   |
      |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",
"""
  +---+
  |   |
  O   |
  |   |
      |
      |
========='
""",
"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",
"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
  =========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""]
#اسوي الستة الكلمات ويختار منها عشوائي
words = ["good","bad","ugly"]
random_word = random.choice(words)

#اضيف فراغات بنفس عدد احرف الكلمة واطبعها بدون علامات تنصيص
display = ["_"] * len(random_word)
print(' '.join(display))
lives = 6 

#قائمة بالحروف المخمنة
guessed_letters = []

#اطبع المرحلة الاولى
print(hangman_stages[0])

#بينما الفراغات متوفرة و الحيوات اكبر من صفر اخلي المستخدم يخمن حرف
while "_" in display and lives > 0:
  guessed = input("please guess a letter:").lower()
  
  #اتاكد اذا الحرف تم استخدامه او تخمينه من قبل
  if guessed in guessed_letters:
    print(f"""
    you already guessed that. try again.
    you have {lives} more tries
    """)
    continue

  #في حال لم يسبق تخمينه اضيفه بالقائمة
  guessed_letters.append(guessed)


  #اتاكد اذا التخخمين صح او غلط
  if guessed not in random_word:
    lives -= 1 
    print(hangman_stages[6 - lives])

  else:
    for position in range(len(random_word)):
      if random_word[position] == guessed:
        display[position] = guessed
        
  print(" ".join(display))
  print(f"you have {lives} more tries")

#اذا المستخدم فاز او خسر 
if lives == 0:
  print("""
  ---------
  you lose!
  ---------
  """)
  print(hangman_stages[-1])
else:
  print("""
  --------
  you win!
  --------
  """)