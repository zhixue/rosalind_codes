with open('rosalind_ba3d.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            num = int(line.rstrip())
        if i == 2:
            string = line.rstrip()

d = {}
current = string[:num-1]
for k in range(1,len(string)-num+2):
    past = current
    current = string[k:k + num-1]
    if past in d:
        #if current in d[past]:
            #continue
        d[past].append(current)
    else:
        d[past] = [current]


for one in sorted(d.keys()):
    out = one + ' -> '
    out += ','.join(sorted(d[one]))
    print(out)

