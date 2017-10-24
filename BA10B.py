with open('rosalind_ba10b.txt') as f:
    i = 0

    pa = ''
    st = ''
    p = {}
    for line in f:
        i += 1
        if i == 1:
            pa = line.rstrip()
        if i == 5:
            st = line.rstrip()
        if i == 10:
            p['Ax'] = float(line.rstrip().split()[1])
            p['Ay'] = float(line.rstrip().split()[2])
            p['Az'] = float(line.rstrip().split()[3])
        if i == 11:
            p['Bx'] = float(line.rstrip().split()[1])
            p['By'] = float(line.rstrip().split()[2])
            p['Bz'] = float(line.rstrip().split()[3])
    print(p)
    result = 1
    for k in range(len(st)):
        result *= p[st[k]+pa[k]]


    print(result)