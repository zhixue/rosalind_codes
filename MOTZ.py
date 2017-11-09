def complement(base1,base2):
    d = {'A':'U','U':'A','C':'G','G':'C'}
    if d[base1] == base2:
        return 1
    else:
        return 0

def motz(seq,temp):
    length = len(seq)
    if length < 2:
        return 1

    if seq in temp:
        return temp[seq]

    counter = motz(seq[1:],temp) # different with cat,be init with motz[n-1]
    for k in range(1,length):  # different with cat,step = 1
        if complement(seq[0],seq[k]):
            counter += motz(seq[1:k],temp) * motz(seq[k+1:],temp)
    temp[seq] = counter % 10**6
    return temp[seq]

with open('rosalind_motz.txt') as f:
    rna = ''
    for line in f:
        if line.startswith('>'):
            continue
        else:
            rna += line.rstrip()

temp = {} # a dictonary store the value of the substring of rna
print(motz(rna,temp))