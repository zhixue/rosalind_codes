seq_list = []
stseq = ''
for line in open('rosalind_tran.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)
sa = seq_list[0]
sb = seq_list[1]




transition = 0
transversion = 0
for i in range(len(sa)):
    if sa[i] != sb[i]:
        if (sa[i]=='A' and sb[i]=='G') or (sa[i]=='G' and sb[i]=='A') \
                or (sa[i]=='C' and sb[i]=='T') or (sa[i]=='T' and sb[i]=='C'):
            transition += 1
        else:
            transversion += 1
print transition*1.0/transversion