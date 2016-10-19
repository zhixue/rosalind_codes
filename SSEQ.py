seq_list = []
stseq = ''
for line in open('rosalind_sseq.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)


S = seq_list[0]
s = seq_list[1]
for start in range(len(S)):
    locations = [0]*len(s)
    find = 0
    for now in range(start,len(S)):
        if S[now] == s[find]:
            locations[find] = str(now+1)
            find += 1
            if find >= len(s):
                break
    if locations[-1] != 0:
        print ' '.join(locations)

