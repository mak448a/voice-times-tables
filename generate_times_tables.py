"""
This file is for generating the the times.json file.
The json file is then used in the quiz files.
"""
import json

times_tables = {}

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for num in numbers:
    times_tables[f"{num}"] = {}
    for num2 in numbers:
        times_tables[f"{num}"][f"{num2}"] = num * num2

print(times_tables)

with open("times.json", "w") as f:
    json.dump(times_tables, f, indent=4)
