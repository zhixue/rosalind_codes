def minEditDist(sm,sn):
    m,n = len(sm)+1,len(sn)+1
    # create a matrix (m*n)
    matrix = [[0]*n for i in range(m)]
    matrix[0][0]=0
    # trace
    tracesm = [['']*n for i in range(m)]
    tracesn = [['']*n for i in range(m)]
    for i in range(1,m):
        matrix[i][0] = matrix[i-1][0] + 1
        tracesm[i][0] = sm[i-1]
        tracesn[i][0] = sm[i-1]
    for j in range(1,n):
        matrix[0][j] = matrix[0][j-1]+1
        tracesm[0][j] = sn[j-1]
        tracesn[0][j] =sn[j-1]
    cost = 0
    for i in range(1,m):
        for j in range(1,n):
            if sm[i-1]==sn[j-1]:
                cost = 0
            else:
                cost = 1
            minstep = min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+cost)
            matrix[i][j]= minstep
            # trace
            if minstep == matrix[i-1][j-1]+cost:
                tracesm[i][j] = tracesm[i-1][j-1] + sm[i-1]
                tracesn[i][j] = tracesn[i - 1][j - 1] + sn[j- 1]
            elif minstep == matrix[i-1][j]+1:
                tracesm[i][j] = tracesm[i-1][j] + sm[i-1]
                tracesn[i][j] = tracesn[i-1][j] + '-'
            elif minstep == matrix[i][j-1]+1:
                tracesm[i][j] = tracesm[i][j-1] + '-'
                tracesn[i][j] = tracesn[i][j-1] + sn[j-1]


    return str(matrix[m-1][n-1]),tracesm[m-1][n-1],tracesn[m-1][n-1]

if __name__ == '__main__':
    with open('rosalind_edta.txt') as f:
        i = 0
        a = []
        b = []
        for line in f:
            i += 1
            if line.startswith('>'):
                if a == []:
                    a.append(line)
                else:
                    b.append(line)
            else:
                if b == []:
                    a.append(line.rstrip())
                else:
                    b.append(line.rstrip())
    a = ''.join(a[1:])
    b = ''.join(b[1:])

    print('\n'.join(minEditDist(a,b)))