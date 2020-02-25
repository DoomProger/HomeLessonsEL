from itertools import cycle

i = 0
for el in cycle([1, 2, '33', 2.3, 'nice day']):
    if i > 10:
        break
    print(el)
    i += 1
