import itertools
n = 5
p_list_number = [str(x) for x in range(1,n+1)]
n_list_number = [str(x) for x in range(-1,-n-1,-1)]
n_list_number.extend(p_list_number)

a = list(itertools.permutations(n_list_number,n))
result = []

for one in range(len(a)):
    result.append(list(a[one]))
for one in range(len(a)):
    for i in range(len(a[one])-1):
        for k in range(i+1,len(a[one])):
            if int(a[one][i]) + int(a[one][k]) == 0:
                result[one] = ''
                break
                break
line = 0
for q in result:
    if q != '':
        line += 1

fp = open('out.txt','w')
fp.write(str(line)+'\n')
for one in result:
    if one != '':
        fp.write(' '.join(one)+'\n')
fp.close()