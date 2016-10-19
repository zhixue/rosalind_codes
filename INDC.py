from math import factorial
from math import log10
n = 50

s = 0
for j in range(1,2*n+1):
    p = 0
    for i in range(j,2*n+1):
        p += factorial(2*n)/(factorial(i)*factorial(2*n-i))*0.5**(2*n)
    print log10(p),