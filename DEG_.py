ans = [0] * 5000
read = []
i = 1
for line in open('rosalind_deg.txt'):
    if i == 1:
        i = 2
        continue
    read.append([int(x) for x  in line.rstrip().split(' ')])
#print(read)
for one in read:
    ans[one[0]] += 1
    ans[one[1]] += 1
for a in ans[1:]:
    if a == 1:
        a = 0


for x in ans[1:]:
    if x == 0:
        break
    else:
        print(x,end=' ')