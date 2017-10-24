with open('rosalind_test.txt') as f:
    i = 0
    old = []
    new = []
    for line in f:
        i += 1
        if i % 3 == 1:
            old = [int(x) for x in line.rstrip().split(' ')]
        if i % 3 == 2:
            new = [int(x) for x in line.rstrip().split(' ')]

            toR = 0
            toL = 0
            for m in range(len(new)):
                for n in range(len(old)):
                    if old[n] == new[m]:
                        if m < n:
                            toR += n - m
                        else:
                            toL += m - n
                        break
            #print(toL, toR)
            #if toL == toR:
                #print(toL,end=' ')
            #else:
                #pass
                #print(toL,toR,end=' ')
