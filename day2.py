import os.path

with open(os.path.join('inputs', 'inputDay2.txt')) as f:
    game_rounds = list(f.read().split('\n'))

""" PART 1 """
# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won
cases = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3,
         'B X': 1, 'B Y': 2 + 3, 'B Z': 3 + 6,
         'C X': 1 + 6, 'C Y': 2, 'C Z': 3 + 3}

total = 0
for g in game_rounds:
    total += cases[g]
print(total)

""" PART 2 """
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
cases = {'A X': 'Z', 'A Y': 'X', 'A Z': 'Y',
         'B X': 'X', 'B Y': 'Y', 'B Z': 'Z',
         'C X': 'Y', 'C Y': 'Z', 'C Z': 'X'}

result_weight = {'X': 0, 'Y': 3, 'Z': 6}
pick_weight = {'X': 1, 'Y': 2, 'Z': 3}

total2 = 0
for g in game_rounds:
    total2 += pick_weight[cases[g]] + result_weight[g[-1]]
print(total2)