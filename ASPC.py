from math import factorial
n=1790
k=915
s = 0
for i in range(k,n+1):
    s = s + factorial(n)/(factorial(i)*factorial(n-i)) % 1000000
print s % 1000000
