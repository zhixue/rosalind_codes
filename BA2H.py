inf = 1000000000000000000000
def distancebetweenpatternandstrings(pattern,dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        hamdistance = inf
        for pos in range(len(string)-k+1):
            temppattern = string[pos:pos+k]
            if hamdistance > hamming_dis(pattern,temppattern):
                hamdistance = hamming_dis(pattern,temppattern)
        distance += hamdistance
    return distance

def hamming_dis(sa,sb):
    c = 0
    for i in range(len(sa)):
        if sa[i] != sb[i]:
            c = c + 1
    return c

with open('rosalind_ba2h.txt') as f:
    ptn = f.readline().rstrip()
    dnasrings = [x.rstrip() for x in f.readline().split(' ')]
print(distancebetweenpatternandstrings(ptn,dnasrings))