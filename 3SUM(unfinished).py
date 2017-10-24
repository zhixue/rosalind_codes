l = 0
n = 0
with open('rosalind_3sum.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            l = int(line.rstrip().split(' ')[0])
            n = int(line.rstrip().split(' ')[1])
        else:
            temp = [int(x) for x in line.rstrip().split(' ')]
            flag = -1
            for u in range(n):
                for v in range(u+1,n):
                    for w in range(v+1,n):
                        if temp[u] + temp[v] + temp[w] == 0:
                            print(' '.join((str(u+1),str(v+1),str(w+1))))
                            flag = 1
                            break
                    if flag == 1:
                        break
                if flag == 1:
                    break
            if flag == -1:
                print('-1')

