import itertools
def match(s1,s2,mistake):
    mis = 0
    for k in range(len(s1)):
        if s1[k] != s2[k]:
            mis += 1
            if mis > mistake:
                return 0
    return 1

def count(string,pattern,mistake):
    counter = 0
    counter = sum([match(string[n:n+len(pattern)],pattern,mistake) for n in range(len(string)-len(pattern)+1)])
    return counter

def select(string,patterns,mistake):
    result = []
    for one in patterns:
        if count(string,one,mistake)>0:
            result.append(one)
    return result

with open('rosalind_ba2a.txt') as f:
    i = 0
    codna = []
    for line in f:
        i += 1
        if i == 1:
            temp = line.rstrip().split()
            length = int(temp[0])
            mis = int(temp[1])
        else:
            codna.append(line.rstrip())

l = ['A','C','G','T']
r1 = [''.join(x) for x in itertools.product(*[l] * int(length))]


for dna in codna:
    r1 = select(dna,r1,mis)
print(' '.join(r1))