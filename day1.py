import os.path

with open(os.path.join('inputs', 'inputDay1.txt')) as f:
    calories = list(map(str.split, f.read().split('\n\n')))

total_calories = sorted([sum(map(int, c)) for c in calories])

# part 1 - find elf with max calories
max_calories = total_calories[-1]
print(max_calories)

# part 2 - find 3 top elfs with most calories
max_3_calories = sum(total_calories[-3:])
print(max_3_calories)