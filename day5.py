import os.path
import re
import copy

with open(os.path.join('inputs', 'inputDay5', 'stacks.txt'), newline='\n') as inputfile:
    rows = [line for line in inputfile]

stacks = []

for row in rows:
    stack = [row[i:i+4].strip().replace('[', '').replace(']', '') for i in range(0, len(row), 4)]
    if len(stack) == 8:
        stack.append('')
    stacks.append(stack)

queues = {}

for n in stacks[-1]:
    n = int(n)
    queue = []
    for i in range(len(stacks[-1]) - 2, -1, -1):
        queue.append(stacks[i][n - 1])
    while '' in queue:
        queue.remove('')
    queues[n] = queue

with open(os.path.join('inputs', 'inputDay5', 'operations.txt'), newline='\n') as inputfile:
    operations = [re.sub('(move|from|to)', '', line).split() for line in inputfile]

# part 1
moved_queues = copy.deepcopy(queues)
for operation in operations:
    for moveTimes in range(0, int(operation[0])):
        moved_queues[int(operation[2])].append(moved_queues[int(operation[1])].pop())


result = ''.join([v[-1] for v in moved_queues.values()])
print(result)

# part 2
moved_queues2 = copy.deepcopy(queues)
for operation in operations:
    moveTimes = int(operation[0])
    moved_queues2[int(operation[2])] = moved_queues2[int(operation[2])] + moved_queues2[int(operation[1])][-moveTimes:]
    del moved_queues2[int(operation[1])][len(moved_queues2[int(operation[1])]) - moveTimes:]

result2 = ''.join([v[-1] for v in moved_queues2.values()])
print(result2)