import os.path

with open(os.path.join('inputs', 'inputDay6.txt'), newline='\n') as inputfile:
    string = inputfile.read()

for i in range(3, len(string)):
    s = {string[j] for j in range(i, i - 4, -1)}
    if len(s) == 4:
        print("part 1:", i + 1)
        break

for i in range(3, len(string)):
    s = {string[j] for j in range(i, i - 14, -1)}
    if len(s) == 14:
        print("part 2:", i + 1)
        break


