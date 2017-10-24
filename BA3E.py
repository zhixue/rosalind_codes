with open('rosalind_ba3e.txt') as f:
    ls = [x.rstrip() for x in f.readlines()]

d = {}
num = len(ls[0])
for i in ls:
    on = i[:-1]
    down = i[1:]
    if on in d:
        d[on].append(down)
    else:
        d[on] = [down]





for one in sorted(d.keys()):
    out = one + ' -> '
    out += ','.join(sorted(d[one]))
    print(out)

