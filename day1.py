import os.path

with open(os.path.join('inputs', 'inputDay1.txt')) as f:
    calories = list(map(str.split, f.read().split('\n\n')))

total_calories = [sum(map(int, c)) for c in calories]
max_calories = max(total_calories)
print(max_calories)