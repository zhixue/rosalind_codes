with open('rosalind_ps.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            a = sorted([int(x) for x in line.rstrip().split(' ')])
        if i == 3:
            printk = int(line.rstrip())
            a = a[:printk]
            print(' '.join([str(x) for x in a]))
