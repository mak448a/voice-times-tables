import json
import os
import random


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
    try:
        player_answer = input("Type your answer: ")
        player_answer = int(player_answer)
        break
    except ValueError:
        print("Please enter a number.")
        speak("Please enter a number.")
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

os.system("python3 quiz.py")
