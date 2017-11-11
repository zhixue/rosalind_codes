with open('rosalind_ba5b.txt') as f:
    n,m = map(int,f.readline().rstrip().split(' '))
    Down = []
    Right = []
    for i in range(n):
        Down.append(list(map(int,f.readline().rstrip().split(' '))))
    f.readline()
    for i in range(n+1):
        Right.append(list(map(int,f.readline().rstrip().split(' '))))
matrix = [[0 for x in range(m+1)] for y in range(n+1)]

# init
for i in range(1,m+1):
    matrix[0][i] = matrix[0][i-1] + Right[0][i-1]
for j in range(1,n+1):
    matrix[j][0] = matrix[j-1][0] + Down[j-1][0]

# start
for j in range(1,n+1):
    for i in range(1,m+1):
        matrix[j][i] = max(matrix[j][i-1]+Right[j][i-1],matrix[j-1][i]+Down[j-1][i])

print(matrix[n][m])