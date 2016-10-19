from math import sqrt

def fun(a,b,c):
    return 1-(-b-sqrt(b*b-4*a*c))/2.0/a

for line in open('rosalind_afrq.txt'):
    aa_plist = [float(x) for x in line.rstrip().split(' ')]


for k in aa_plist:
    ak = 1
    bk = -2*(1-k)-4*k
    ck = (1-k)**2
    print fun(ak,bk,ck),