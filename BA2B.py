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

def hamming_dis(sa,sb):
    c = 0
    for i in range(len(sa)):
        if sa[i] != sb[i]:
            c = c + 1
    return c

with open('rosalind_ba2b.txt') as f:
    i = 0
    codna = []
    for line in f:
        i += 1
        if i == 1:
            temp = line.rstrip().split()
            length = int(temp[0])
            mis = 0
        else:
            codna.append(line.rstrip())

l = ['A','C','G','T']
r1 = [''.join(x) for x in itertools.product(*[l] * int(length))]


patterns = [select(dna,r1,mis) for dna in codna]


r1 = []
for one in patterns:
    r1 += one

#print(r1)
#print(patterns)
mindis = 10000000000000
out = ''
for one in r1:
    dis = 0
    for pattern in patterns:
        dis += min([hamming_dis(one,another) for another in pattern])

    if dis <= mindis:
        out = one
        mindis = dis


print(out)