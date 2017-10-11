with open('rosalind_par.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            print(' '.join([str(k) for k in sorted([int(x) for x in line.split(' ')])]))