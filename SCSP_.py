i = 1
for line in open('rosalind_test.txt'):
    if i == 1:
        s1 = line.rstrip().split(' ')
    if i == 2:
        s2 = line.rstrip().split(' ')
    i += 1
#init
s1 = s1[0]
s2 = s2[0]
n1 = len(s1) + 1
n2 = len(s2) + 1
a = [[0] * n2] * n1  # n2 x n1 matrix
for i in range(1,n2):
    a[0][i] = i
for j in range(1,n1):
    a[j] = [j] * n2
scs = ''
print(a)
#start
i,j=1,1
while(i<=n2):
    while(j<=n1):
        print(s1[j-1],s2[i-1])
        if s1[j-1] == s2[i-1]:
            p = 1
        else:
            p = 2
        a[i][j] = min(a[i-1][j]+1,a[i-1][j-1]+p,a[i][j-1]+1)
        if a[i][j] == a[i-1][j-1]+p:
            scs += s1[j-1]
            i += 1
            j += 1
        elif a[i][j] == a[i-1][j]+1:
            scs += s2[i-1]
            i += 1
        else:
            scs += s1[j-1]
            j += 1

print(scs)