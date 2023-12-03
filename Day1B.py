total = 0
number_words = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

with open("input.txt") as my_file:
    for line in my_file:
        s1 = 0
        for key, value in number_words.items():
            if key in line:
                line = line.replace(key, key[0] + value + key[-1])
        s1=''.join(c for c in line if c.isdigit())
        cord = list(s1)
        if len(cord) == 1:
            cord += cord
        res = [cord[i] for i in (0, -1)]
        num = int(''.join(res))
        total += num
print('Total:', total)
