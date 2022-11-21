import json
import os
import random

from word2num import parse_int
from voice_recognition import listen


def speak(words):
    os.system(f'espeak "{words}"')


with open("times.json") as f:
    times_tables = json.load(f)

num1 = str(random.randint(0, 12))
num2 = str(random.randint(0, 12))

question = f"What's {num1} times {num2}?"

answer = times_tables[num1][num2]

print(question)
speak(question)

player_answer = None

while True:
    player_answer_returned = False
    try:
        player_answer = listen()
        # Convert the words into a number
        player_answer = parse_int(player_answer)
        player_answer_returned = player_answer
        print(player_answer)
        player_answer = int(player_answer)
        break
    except ValueError:
        if player_answer_returned:
            if player_answer_returned == "nothing":
                continue
        print("Please say a number.")
        speak("Try saying that again.")
        continue

choices = [
    "You got it!",
    "That's it!",
    "That's right.",
    "You've got the right answer.",
    "Correct! You're doing pretty good.",
    "Correct!"
]
choice = random.choice(choices)

if player_answer == answer:
    print(choice)
    speak(choice)
else:
    print(f"It's {answer}, obviously.")
    suck = random.choice(['You suck!', ''])
    if suck:
        print("You suck!")

    speak(f"It's {answer}, obviously. {suck if suck else ''}")

os.system("python3 quiz_voice.py")
