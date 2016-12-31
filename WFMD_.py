from math import factorial
def com(n,k):
    return factorial(n)/factorial(n-k)/factorial(k)

n,m,g,k=6,8,5,5
p = 1 - m / 2.0 / n
plist = [com(2*n,i)*(p**i)*(1-p)**(2*n-i) for i in range(1,2*n+1)]

for genera in range(2,g+1):
    now_plist = []
    for j in range(1,2*n+1):
        now_num = [com(2*n,j)*(x/2.0/n)**j *(1-x/2.0/n)**(2*n-j) for x in range(1,2*n+1)]
        now_plist.append(sum([now_num[i]*plist[i] for i in range(len(now_num))]))
    plist = now_plist

print(sum(plist[k-1:]))