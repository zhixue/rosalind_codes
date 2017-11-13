import sys
sys.setrecursionlimit(10000) #递归深度
def complement(base1,base2):
    d = {'A':['U'],'U':['A','G'],'C':['G'],'G':['C','U']}
    if base2 in d[base1]:
        return 1
    else:
        return 0

def rnas(seq,count = {}):
    length = len(seq)
    if length < 5:
        return 1
    if seq in count:
        return count[seq]
    else:
        count[seq] = rnas(seq[1:],count)
        for pos in range(4,len(seq)):
            if complement(seq[0],seq[pos]):
                count[seq] += rnas(seq[1:pos],count) * rnas(seq[pos+1:],count)
        return count[seq]


with open('rosalind_rnas.txt') as f:
    rna = ''
    for line in f:
        if line.startswith('>'):
            continue
        else:
            rna += line.rstrip()

temp = {} # a dictonary store the value of the substring of rna
print(rnas(rna))