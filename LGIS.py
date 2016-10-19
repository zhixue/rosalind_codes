def longest_sub_increase_seq(array):

    length = len(array)
    x=[1 for i in range(length)]
    z=[0 for i in range(length)]
    for i in range(1,length):
        index=i
        maxnum=1
        for j in range(i):
            if array[i]>array[j]:
                if maxnum<x[j]+1:
                    index=j
                    maxnum=x[j]+1

        z[i]=index
        x[i]=maxnum
    maxvlaue=max(x)

    return_value=[]
    for i in range(length):
        vv=[]
        if x[i]==maxvlaue:
            j=i
            while z[j]!=j:
                vv.append(array[j])
                j=z[j]
            else:
                vv.append(array[j])
            return_value.append(vv)

    return return_value[0]

i = 0
for line in open('rosalind_lgis.txt'):
    i += 1
    if i == 1:
        n = int(line.strip('\n'))
    else:
        per = line.strip('/n').split(' ')
per = [int(x) for x in per]


print ' '.join(str(x) for x in longest_sub_increase_seq(per)[::-1])
print ' '.join(str(x) for x in longest_sub_increase_seq(per[::-1]))