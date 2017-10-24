with open('rosalind_test.txt') as f:
    ls = [x.rstrip() for x in f.readlines()]

    length = int(ls[0])
    ls = ls[1:]

print(ls)
out = ls[0]
ls = sorted(ls[1:])
print(ls)

while ls:
    i = 0
    l = len(ls)
    while(i<l):
        print(out,ls[i])
        if out[:3] == ls[i][-3:]:
            out = ls[i][:-3] + out
            ls.pop(i)
            l -= 1
        elif out[-3:] == ls[i][:3]:
            out = out + ls[i][:3]
            ls.pop(i)
            l -= 1
        else:
            i += 1

print(out)