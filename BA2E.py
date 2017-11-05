def greedymotifsearch(dna,k,t):
    best = [s[:k] for s in dna]
    for i in range(len(dna[0])-k+1):
        tempbest = [dna[0][i:i+k]]
        for m in range(1,t):
            matrix = motifsToProfile(tempbest)  # different from ba2d
            tempbest.append(profileMostProbablekmer(dna[m],k,matrix))
        if score(tempbest) < score(best):
            best = tempbest
    return best

def score(motifs):
    z = zip(*motifs)
    thescore = 0
    for string in z:
        score = len(string) - max([string.count('A'), string.count('C'), string.count('G'), string.count('T')])
        thescore += score
    return thescore

def motifsToProfile(motifs):
    d = {}
    n = float(len(motifs))
    z = list(zip(*motifs))
    for i in range(len(z)):
        d.setdefault('A', []).append((z[i].count('A')+1)/n/2)
        d.setdefault('C', []).append((z[i].count('C')+1)/n/2)
        d.setdefault('G', []).append((z[i].count('G')+1)/n/2)
        d.setdefault('T', []).append((z[i].count('T')+1)/n/2)
    return d

def profileMostProbablekmer(text, k , matrix):
    maxp = None
    probablekmer = None
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        pt = 1
        for j in range(k):
            p = matrix[kmer[j]][j]
            pt *=p
        if maxp == None or pt > maxp:
            maxp = pt
            probablekmer = kmer
    return probablekmer

with open('rosalind_ba2e.txt') as f:
    k,t = map(int,f.readline().rstrip().split(' '))
    strings = [st.rstrip() for st in f.readlines()]
print('\n'.join(greedymotifsearch(strings,k,t))) # bug: may be wrong , try several times