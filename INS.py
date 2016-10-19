l = 0
a = []
for line in open('rosalind_ins.txt'):
    if l == 0:
        l = int(line.strip('\n'))
    else:
        a = [int(x) for x in line.split(' ')]

times = 0
for i in range(1,l):
    k = i
    while (k>0 and a[k]<a[k-1]):
        a[k],a[k-1] = a[k-1],a[k]
        k -= 1
        times += 1
print times