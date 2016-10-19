def f(n,k):
    s = [0]*(k+1)
    s[0] = 1
    for x in range(1,n):
        s[1:k+1] = s[0:k]
        s[0] = sum(s[2:])
        #print x+1,s
    return sum(s[:-1])
#n=m-1
print f(100,50)