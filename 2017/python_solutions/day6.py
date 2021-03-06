def format_input(x):
    delimiter = '\t' if '\t' in x else ' '
    return [int(n) for n in x.split(delimiter) if n != '']

def empty_box(banks, start):
    count = banks[start]
    banks[start] = 0
    for _ in range(count):
        start = start + 1 if start + 1 < len(banks) else 0
        banks[start] += 1
    return banks

def find_box_to_empty(banks):
    return banks.index(max(banks))

def solve_1(x):
    x = format_input(x)
    already_seen = []
    count = 0
    while x not in already_seen and count < 20000:
        already_seen.append(x[:])
        start = find_box_to_empty(x)
        x = empty_box(x, start)
        count += 1
    return count

def solve_2(x):
    x = format_input(x)
    already_seen = []
    count = 0
    while x not in already_seen and count < 20000:
        already_seen.append(x[:])
        start = find_box_to_empty(x)
        x = empty_box(x, start)
        count += 1
    start_loop = already_seen.index(x)
    end_loop = len(already_seen)
    return end_loop - start_loop
