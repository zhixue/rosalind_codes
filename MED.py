with open('rosalind_med.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 3:
            k = int(line.rstrip())
        if i == 2:
            ls = sorted([int(x) for x in line.rstrip().split(' ')])
    print(ls[k-1])