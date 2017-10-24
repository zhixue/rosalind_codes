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
    return sum([match(string[n:n+len(pattern)],pattern,mistake) for n in range(len(string)-len(pattern))])

def reverse(string):
    return string[::-1].replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()



with open('rosalind_ba1j.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            string = line.rstrip()
        if i == 2:
            length = int(line.rstrip().split(' ')[0])
            mis = int(line.rstrip().split(' ')[1])


l = ['A','C','G','T']
r1 = [''.join(x) for x in itertools.product(*[l] * int(length))]

times = 0
for one in r1:
    temp = count(string,one,mis) + count(string,reverse(one),mis)
    if temp >= times:
        if temp > times:
            print('\n')
            print(temp,end = '\n')
        times = temp
        print(one,end = ' ')
