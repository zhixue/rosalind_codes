import itertools
set1 = []
n = 6 #change
for i in range(1,n+1):
    set1.append(i)
a = itertools.permutations(set1,n)
k = 0
for one in list(a):
    print ' '.join(map(str,list(one)))
    k += 1
print k
