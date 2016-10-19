seq_list = []
stseq = ''
for line in open('rosalind_grph.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append([stname,stseq])
            stseq = ''
        stname = line[1:-1]
    else:
        stseq = stseq + line.strip('\n')
seq_list.append([stname,stseq])
l = len(seq_list)

for i in range(0,l):
    for j in range(0,i):
        if seq_list[i][1] == seq_list[j][1]:
            continue
        if seq_list[i][1][0:3] == seq_list[j][1][-3:]:
            print seq_list[j][0],seq_list[i][0]
        if seq_list[i][1][-3:] == seq_list[j][1][0:3]:
            print seq_list[i][0],seq_list[j][0]
