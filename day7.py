import os.path

with open(os.path.join('inputs', 'inputDay7.txt'), newline='\n') as inputfile:
    operations = [line.strip().split() for line in inputfile]

curr_dir = []
reading = False
dirs = {}

for operation in operations:
    if len(operation) == 3 and operation[0] == '$':
        if operation[1] == 'cd':
            if operation[2] == '..':
                curr_dir.pop()
            else:
                curr_dir.append(operation[2])

    elif len(operation) == 2 and operation[0] != '$':
        dir_path = '/'.join(curr_dir)
        operation[1] = dir_path + '/' + operation[1]
        if dir_path in dirs:
            dirs[dir_path].append(operation)
        else:
            dirs[dir_path] = [operation]
sizes = {}


def get_size(contents):
    s = 0
    for content in contents:
        if content[0] == 'dir':
            print(content[1])
            if content[1] in sizes:
                s += sizes[content[1]]
            else:
                size = get_size(dirs[content[1]])
                sizes[content[1]] = size
                s += size
        else:
            s += int(content[0])
    return s


for d, files in dirs.items():
    if d in sizes:
        continue
    sizes[d] = get_size(files)


# part 1
total = 0
for v in sizes.values():
    if v <= 100000:
        total += v
print('part 1:', total)

# part 2
space_needed = 30000000 - (70000000 - sizes['/'])
sizes_values = sizes.values()
min_val = max(sizes_values)
for i in sizes_values:
    if min_val > i > space_needed:
        min_val = i
print('part 2:', min_val)