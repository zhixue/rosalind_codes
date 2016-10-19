def reverse_dna(string):
    string1 = string.replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()
    return string1[::-1]


def similar(a,b):
    n = len(a)
    re_b = reverse_dna(b)
    mark1 = 0
    mark2 = 0
    for i in range(n):
        if a[i] == b[i]:
            mark1 += 1
        if a[i] == re_b[i]:
            mark2 += 1
    if mark1 == n-1:
        return 1
    if mark2 == n-1:
        return 2
    else:
        return 0


seq_list = []
stseq = ''
for line in open('rosalind_corr.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)


corr_list = []
wrong_list = []
for i in range(len(seq_list)-1):
    for j in range(i+1,len(seq_list)):
        if seq_list[i]==seq_list[j] or seq_list[i]==reverse_dna(seq_list[j]):
            corr_list.append(seq_list[i])
for one in seq_list:
    if not((one  in corr_list) or (reverse_dna(one)  in corr_list)):
        wrong_list.append(one)
corr_list = list(set(corr_list))
wrong_list = list(set(wrong_list))

for one in wrong_list:
    for another in corr_list:
        if similar(one,another) == 1:
            print one+'->'+another
        if similar(one,another) == 2:
            print one+'->'+reverse_dna(another)

