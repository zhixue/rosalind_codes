def mark(a,b,mutation):
    mis = 0
    for m in range(len(a)):
        if a[m] != b[m]:
            mis += 1
        if mis > mutation:
            return  False
        if m == len(a)-1:
            return True
l = 0
for line in open('rosalind_ba1i.txt'):
    l += 1
    if l == 2:
        k = int(line.rstrip().split(' ')[0])
        d = int(line.rstrip().split(' ')[1])
    if l == 1:
        string = line.rstrip()
#print string,k,d
count_sub = {}
for i in range(len(string)-k):
    sub_s = string[i:i+k]
    count = -1
    for j in range(len(string)-k+1):
        now_sub = string[j:j+k]
        if mark(sub_s,now_sub,d):
            count += 1

    count_sub[sub_s] = count

maxcount = 0
for key,value in count_sub.items():
    if value >= maxcount:
        maxcount = value
        maxsub = key
        print value,key



