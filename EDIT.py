def minEditDist(sm,sn):
    m,n = len(sm)+1,len(sn)+1
    # create a matrix (m*n)
    matrix = [[0]*n for i in range(m)]
    matrix[0][0]=0
    for i in range(1,m):
        matrix[i][0] = matrix[i-1][0] + 1
    for j in range(1,n):
        matrix[0][j] = matrix[0][j-1]+1
    cost = 0
    for i in range(1,m):
        for j in range(1,n):
            if sm[i-1]==sn[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+cost)
    return matrix[m-1][n-1]


def editdis(a,b):
    x = [[0 for x in range(len(b) + 1)] for y in range(len(a) + 1)]
    for i in range(0, len(a) + 1):
        for j in range(0, len(b) + 1):
            if i == 0 or j == 0:
                x[i][j] = max(i, j)
            else:
                x[i][j] = min(x[i - 1][j] + 1, x[i][j - 1] + 1, x[i - 1][j - 1] + ((0 if a[i - 1] == b[j - 1] else 1)))
    return x[len(a)][len(b)]

with open('rosalind_edit.txt') as f:
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



print(editdis(b,a))

print(minEditDist(a,b))


import editdistance
print(editdistance.eval(a, b))
