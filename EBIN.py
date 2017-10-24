with open('rosalind_ebin.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            times = float(line.rstrip().split()[0])
        else:
            temp = [float(x) for x in line.rstrip().split()]
            for one in temp:
                print(times*one,end=' ')