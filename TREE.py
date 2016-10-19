i = 0
tree = []
for line in open('rosalind_tree.txt'):
    i += 1
    if i == 1:
        n = int(line.strip('\n'))
    elif i == 2:
        tree.append(set([int(x) for x in line.strip('\n').split(' ')]))
    else:
        temp = set([int(x) for x in line.strip('\n').split(' ')])
        for k in range(len(tree)):
            if temp & tree[k] != set([]):
                tree[k] = temp | tree[k]
                break
            if k == len(tree) - 1:
                tree.append(temp)

#get the not single nunber list
not_single = []
for one in tree:
    for x in one:
        not_single.append(x)

print len(tree)+(n - len(not_single))-1