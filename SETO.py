i = 0
for line in open('rosalind_seto.txt'):
    i += 1
    if i == 1:n = int(line.strip('\n'))
    if i == 2:set1 = line[1:-2].split(', ')
    if i == 3:set2 = line[1:-1].split(', ')

for x in [set1,set2]:
    for i in range(len(x)):
        x[i] = int(x[i])
setall = set([x for x in range(1,n+1)])
set1 = set(set1)
set2 = set(set2)

print '{'+str(set1 | set2)[5:-2]+'}'
print '{'+str(set1 & set2)[5:-2]+'}'
print '{'+str(set1 - set2)[5:-2]+'}'
print '{'+str(set2 - set1)[5:-2]+'}'
print '{'+str(setall - set1)[5:-2]+'}'
print '{'+str(setall - set2)[5:-2]+'}'