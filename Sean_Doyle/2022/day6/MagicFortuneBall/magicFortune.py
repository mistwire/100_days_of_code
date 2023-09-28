#!/usr/bin/env python3

import random, time


def slowSpacePrint(text, interval=0.1):
    """Slowly display text with spaces in between each letter and lowercase letter i's."""

    for character in text:
        if character == "I":
            print("i ", end="", flush=True)
        else:
            print(character + " ", end="", flush=True)
        time.sleep(interval)
    print("\n" * 2)


slowSpacePrint("MAGIC FORTUNE BALL, BY AL SWEIGART, ADOPTED BY SEAN DOYLE")
time.sleep(0.5)
slowSpacePrint("ASK ME YOUR YES/NO QUESTION.")
input("> ")

replies = [
    "LET ME THINK ON THIS...",
    "AN INTERESTING QUESTION...",
    "HMMM... ARE YOU SURE YOU WANT TO KNOW...",
    "DONT YOU THINK SOME THINGS IN LIFE ARE BEST UNKNOWN?...",
    "YES...NO...MAYBE...LET ME THINK ON THIS...",
    "AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER TO THAT YOU ARE SEEKING?...",
    "YOU MAY WANT TO SIT DOWN FOR THIS...",
]

slowSpacePrint("." * random.randint(4, 10), 0.7)

slowSpacePrint("I HAVE AN ANSWER...", 0.2)
time.sleep(1)
answers = [
    "YES, FOR SURE",
    "MY ANSWER IS NO",
    "ASK ME LATER",
    "I AM PROGRAMMED TO SAY YES",
    "THE STARS SAY YES, BUT I SAY NO",
    "FOCUS AND ASK ONCE MORE",
    "DOUBTFUL",
    "SIGNS POINT TO YES",
    "IT APPEARS SO",
    "I AM LEANING TOWARDS NO",
]
slowSpacePrint(random.choice(answers), 0.05)
