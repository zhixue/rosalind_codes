class Node(object):
    def __init__(self,name = None):
        self.name = name
        self.degree = 0
        self.neighbor = []

    def __repr__(self):
        return str(self.degree)+'  '+str(len(self.neighbor))

read = []
i = 1
for line in open('rosalind_ddeg.txt'):
    if i == 1:
        i = int(line.rstrip().split(' ')[0])
        continue
    read.append([int(x) for x  in line.rstrip().split(' ')])

ans = [Node()  for  i in range(i+1)]
#print(read)
for  one in read:
    ans[one[0]].degree += 1
    ans[one[0]].neighbor.append(ans[one[1]])
    ans[one[1]].degree += 1
    ans[one[1]].neighbor.append(ans[one[0]])

for x in ans[1:]:
        print(sum([it.degree for it in x.neighbor]),end=' ')