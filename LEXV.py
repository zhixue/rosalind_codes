import itertools
for line in open('rosalind_lexv.txt'):
    if line[0].isdigit():
        n = int(line.strip('\n'))
    else:
        string = line.strip('\n').split(' ')
        l = len(string)
result = []
for i in range(1,n+1):
    for m in [''.join(m) for m in itertools.product(*[string] * i)]:
        result.append(m+str(' '*(n-len(m))))
d = {' ':0}
for i in range(len(string)):
    d[string[i]] = i + 1
for i in range(len(result)):
    value_i = 0
    for x in range(n):
        value_i += d[result[i][x]]*(l+1)**(n-x-1)
    for j in range(len(result)-1,i,-1):
        value_j = 0
        for x in range(n):
            value_j += d[result[j][x]]*(l+1)**(n-x-1)
        if value_i > value_j:
            result[i],result[j] = result[j],result[i]
            value_i,value_j = value_j,value_i
fp = open('out.txt','w')
for x in result:
    fp.write(x.strip(' ')+'\n')
fp.close()