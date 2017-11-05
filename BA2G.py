import random
def randomkmers(dna,k):
    motifs = []
    for one in dna:
        pos = random.randrange(0,len(dna[0])-k+1)
        motifs.append(one[pos:pos+k])
    return motifs

def gibbssampler(dna,k,t,N):
    motifs = randomkmers(dna,k)
    best = motifs
    for j in range(N):
        i = random.randrange(0,t)
        motifs.pop(i)
        matrix = motifsToProfile(motifs)
        motifi = profileRandomlyGeneratedkmer(dna[i],k,matrix)
        motifs.insert(i,motifi)
        if score(motifs) < score(best):
            best = motifs
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

def Random(p):
    wheel = [0]*(len(p)+1)
    s = sum(p)
    if s!= float(1):
        p = [float(i)/sum(p) for i in p]
    for index in range(len(p)):
        wheel[index+1] = wheel[index] + p[index]
    r = random.random() # 0 and 1
    for i in range(len(wheel)-1):
        if wheel[i] < r < wheel[i+1]:
            result = i
    return result

def profileRandomlyGeneratedkmer(text, k , matrix):
    prob = []
    for i in range(len(text)-k+1):
        kmer = text[i:i+k]
        pt = 1
        for j in range(k):
            p = matrix[kmer[j]][j]
            pt *=p
        prob.append(pt)
    kmer_index = Random(prob)
    randomkmer = text[kmer_index:kmer_index+k]
    return randomkmer

def runrandomtimes(dna,k,t,N,times):
    bestmotifs = []
    highscore = None
    for i in range(int(times)):
        tempmotifs = gibbssampler(dna,k,t,N)
        tempscore = score(tempmotifs)
        if highscore == None or highscore > tempscore:
            highscore = tempscore
            bestmotifs = tempmotifs
    return bestmotifs

with open('rosalind_ba2g.txt') as f:
    k,t,N = map(int,f.readline().rstrip().split(' '))
    strings = [st.rstrip() for st in f.readlines()]
print('\n'.join(runrandomtimes(strings,k,t,N,20)))
