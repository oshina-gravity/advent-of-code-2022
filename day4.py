import os.path

with open(os.path.join('inputs', 'inputDay4.txt')) as f:
    sessions = list(f.read().split('\n'))

sessions = [s.split(',') for s in sessions]

# part 1
total = 0
for s in sessions:
    first_elf = s[0].split('-')
    second_elf = s[1].split('-')
    if int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1]):
        total += 1
    elif int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1]):
        total += 1
print(total)

# part 2
total2 = 0
for s in sessions:
    first_elf = s[0].split('-')
    second_elf = s[1].split('-')

    overlapping_sessions = {i for i in range(int(first_elf[0]), int(first_elf[1]) + 1)}.intersection({i for i in range(int(second_elf[0]), int(second_elf[1]) + 1)})
    if len(overlapping_sessions) > 0:
        total2 += 1

print(total2)