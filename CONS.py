seq_list = []
stseq = ''
for line in open('rosalind_cons.txt'):
    if line[0] == '>':
        #stname = line[1:-1]
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)
mostpro_seq = ''
ACGT=[]
for k in range(len(seq_list[0])):
    a,c,g,t = 0,0,0,0
    for one in seq_list:
        if one[k] == 'A':
            a += 1
        if one[k] == 'C':
            c += 1
        if one[k] == 'G':
            g += 1
        if one[k] == 'T':
            t += 1
    ACGT.append([a,c,g,t])
    q = ''
    if a == max([a,c,g,t]):
        q = 'A'
    if c == max([a,c,g,t]):
        q = 'C'
    if g == max([a,c,g,t]):
        q = 'G'
    if t == max([a,c,g,t]):
        q = 'T'
    mostpro_seq = mostpro_seq + q
print mostpro_seq

for m in zip(*ACGT):

    out =' '.join(str(i) for i in m)
    print out


