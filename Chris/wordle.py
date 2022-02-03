import random
import sys

words = []

with open('/usr/share/dict/words', 'r') as f:
    for line in f:
        if len(line.strip()) == 5:
            words.append(line.strip().upper())
actual = words[random.randint(0, len(words) - 1)]
max_guess = 0
if len(sys.argv) > 1 and sys.argv[1] == 'unlimited':
    max_guess = 999999
guess_count = 0
max_guess = 6
while True:
    guess_count += 1
    if guess_count <= max_guess:
        print("Enter your guess ({} / {}):".format(guess_count, max_guess))
        guess = input()
        guess = guess.upper()
        if guess in words:
            output = ""
            remaining = ""
            if actual == guess:
                print("You guessed right!")
                for i in range(len(actual)):
                    output += "\033[30;102m {} \033[0m".format(guess[i])
                print(output)
                break
            else:
                for i in range(len(actual)):
                    if actual[i] != guess[i]:
                        remaining += actual[i]
                for i in range(len(actual)):
                    if actual[i] != guess[i]:
                        if remaining.find(guess[i]) != -1:
                            output += "\033[30;103m {} \033[0m".format(guess[i])
                            remaining = remaining.replace(guess[i], "")
                        else:
                            output += "\033[30;107m {} \033[0m".format(guess[i])
                    else:
                        output += "\033[30;102m {} \033[0m".format(guess[i])
                print(output)
        else:
            print("Please enter a valid word with 5 letters!")
            guess_count -= 1
    else:
        print("You lose! The word is:")
        print(actual)
        break
