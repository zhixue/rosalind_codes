

listall = []
l = 0
for line in open('rosalind_mer.txt'):
    l += 1
    if l == 2:
        listall = [int(x) for x in line.rstrip().split(' ')]
    if l == 4:
        listall.extend([int(x) for x in line.rstrip().split(' ')])

listall = sorted(listall)

print ' '.join([str(x) for x in listall])