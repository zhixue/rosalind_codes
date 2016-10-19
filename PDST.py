seq_list = []
stseq = ''
for line in open('rosalind_pdst.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)


dis_matrix = []
temp_mar = []
n = len(stseq)
for i in range(len(seq_list)):
    for j in range(len(seq_list)):
        dis = 0.0
        for k in range(n):
            if seq_list[i][k] != seq_list[j][k]:
                dis += 1
        temp_mar.append(dis/n)
    dis_matrix.append(temp_mar)
    temp_mar = []


for x in dis_matrix:
    print ' '.join([str(m) for m in x])