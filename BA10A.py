with open('rosalind_ba10a.txt') as f:
    i = 0

    st = ''
    p = {}
    for line in f:
        i += 1
        if i == 1:
            st = line.rstrip()
        if i == 6:
            p['AA'] = float(line.rstrip().split()[1])
            p['AB'] = float(line.rstrip().split()[2])
        if i == 7:
            p['BA'] = float(line.rstrip().split()[1])
            p['BB'] = float(line.rstrip().split()[2])
    print(p)
    result = 0.5
    for k in range(len(st)-1):
        result *= p[st[k:k+2]]


    print(result)