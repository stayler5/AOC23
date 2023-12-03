total = 0

with open("input.txt") as my_file:
    for line in my_file:
        s1=''.join(c for c in line if c.isdigit())
        cord = list(s1)
        if len(cord) == 1:
            cord += cord
        res = [cord[i] for i in (0, -1)]
        num = int(''.join(res))
        total += num

print('Total:', total)