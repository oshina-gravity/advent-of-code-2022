import os.path
from string import ascii_lowercase

total = 0

priorities = {}
for priority, alphabet in enumerate(ascii_lowercase, start=1):
    priorities[alphabet] = priority
    priorities[alphabet.upper()] = priority + 26

with open(os.path.join('inputs', 'inputDay3.txt')) as f:
    puzzles = list(f.read().split('\n'))

# part 1
for p in puzzles:
    total += priorities[(''.join(set(p[0:len(p) // 2]).intersection(p[len(p) // 2:])))]
print(total)

# part 2
total2 = 0
for i in range(0, len(puzzles), 3):
    total2 += priorities[''.join(set.intersection(*map(set, [puzzles[i], puzzles[i + 1], puzzles[i + 2]])))]
print(total2)