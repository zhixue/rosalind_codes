def complement(base1,base2):
    d = {'A':'U','U':'A','C':'G','G':'C'}
    if d[base1] == base2:
        return 1
    else:
        return 0

def cat(seq,temp):
    length = len(seq)
    if length < 2:
        return 1

    if seq in temp:
        return temp[seq]

    counter = 0
    for n in range(1,length,2):
        if complement(seq[0],seq[n]):
            counter += cat(seq[1:n],temp) * cat(seq[n+1:],temp)
    temp[seq] = counter % 10**6
    return temp[seq]


with open('rosalind_cat.txt') as f:
    rna = ''
    for line in f:
        if line.startswith('>'):
            continue
        else:
            rna += line.rstrip()

temp = {} # a dictonary store the value of the substring of rna
print(cat(rna,temp))
