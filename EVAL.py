def read():
    i = 0
    for line in open('rosalind_eval.txt'):
        i += 1
        if i==1:
            length = int(line.rstrip())
        if i==2:
            sub_str = line.rstrip()
        if i==3:
            array = [float(x) for x in line.rstrip().split(' ')]
    return length,sub_str,array

l,s,a = read()
n = l+1-len(s)
cg_n = s.count('C')+s.count('G')
at_n = s.count('A')+s.count('T')

for o in a:
    cg_p = o/2
    at_p = (1-o)/2
    print n*(cg_p**cg_n*at_p**at_n),
