print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = (name1 + name2).lower()
first_digit = 0
for i in names:
  if i in 'true':
    first_digit += 1
second_digit = 0
for i in names:
  if i in 'love':
    second_digit += 1
love_score = int(str(first_digit) + str(second_digit))
if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
