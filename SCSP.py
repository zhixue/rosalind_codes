i = 1
for line in open('rosalind_scsp.txt'):
    if i == 1:
        s2 = line.rstrip().split(' ')
    if i == 2:
        s1 = line.rstrip().split(' ')
    i += 1
#init

s1 = ' '+s1[0]
s2 = ' '+s2[0]
#print(s1,s2)
n1 = len(s1)
n2 = len(s2)
a = [[0 for x in range(n2)] for y in range(n1)]   # n1 x n2 matrix
ka = [['' for x in range(n2)] for y in range(n1)]

for i in range(1,n1):
    a[i][0] = i
    ka[i][0] = s1[i]
for j in range(1,n2):
    a[0][j] = j
    ka[0][j] = s2[j]

#print(a)


#start
i = 1
j = 1

while(i<n1):
    while(j<n2):
        #print(s1[j-1],s2[i-1])
        if s1[i] == s2[j]:
            p = 1
        else:
            p = 2
        a[i][j] = min(a[i-1][j]+1,a[i-1][j-1]+p,a[i][j-1]+1)






        if a[i][j] == a[i][j-1]+1:
            ka[i][j] += ka[i][j-1] + s2[j]

        elif a[i][j] == a[i-1][j]+1:
            ka[i][j] += ka[i - 1][j] + s1[i]

        elif a[i][j] == a[i - 1][j - 1] + p:
            if p == 1:

                ka[i][j] = ka[i - 1][j - 1] + s1[i]
            if p == 2:
                ka[i][j] = ka[i - 1][j - 1] + s1[i] + s2[j]

        j += 1

    i += 1
    j = 1





#print(a)

print(ka[n1-1][n2-1])