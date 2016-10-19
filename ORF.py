def orf(sequence):
    rev_seq = sequence[::-1].replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()
    codonTable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'', 'TAG':'',
    'TGC':'C', 'TGT':'C', 'TGA':'', 'TGG':'W',
    }
    pro_list = []
    for start in range(len(sequence)-3):
        proUeinsequence = ''
        if codonTable[sequence[start:start+3]] == 'M':
            for n in range(start,len(sequence),3):
                if sequence[n:n+3] in codonTable.keys():
                    proUeinsequence += codonTable[sequence[n:n+3]]
                    if codonTable[sequence[n:n+3]] == '':
                        if proUeinsequence != '':
                            pro_list.append(proUeinsequence)
                        break

    for start in range(len(rev_seq)-3):
        proUeinsequence = ''
        if codonTable[rev_seq[start:start+3]] == 'M':
            for n in range(start,len(rev_seq),3):
                if rev_seq[n:n+3] in codonTable.keys():
                    proUeinsequence += codonTable[rev_seq[n:n+3]]
                    if codonTable[rev_seq[n:n+3]] == '':
                        if proUeinsequence != '':
                            pro_list.append(proUeinsequence)
                        break

    return set(pro_list)


seq_list = []
stseq = ''
for line in open('rosalind_orf.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)

proteins = orf(seq_list[0])

for one in proteins:
    print one