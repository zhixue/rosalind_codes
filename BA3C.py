with open('rosalind_ba3c.txt') as f:
    ls = [x.rstrip() for x in f.readlines()]

for i in range(len(ls)):
    for j in range(len(ls)):
        if i == j:
            continue
        if ls[i][1:] == ls[j][:-1]:
            print(ls[i] + ' -> ' + ls[j])

