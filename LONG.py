seq_list = []
stseq = ''
for line in open('rosalind_long.txt'):
    if line[0] == '>':
        if stseq != '':
            seq_list.append(stseq)
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
seq_list.append(stseq)

long_seq = ''

while 1:

    for x in seq_list:
        if long_seq.count(x) > 0:
            seq_list.remove(x)
        else:
            if long_seq == '':
                long_seq = x
            else:
                for i in range(min(len(x),len(long_seq)),0,-1):
                    #print long_seq,x
                    #print long_seq[:i],x[min(len(x),len(long_seq))-i:]
                    #print long_seq[len(long_seq)-i:], x[:i]
                    #print '--------------------------------------',i
                    if (long_seq[:i] == x[min(len(x),len(long_seq))-i:]):
                        long_seq = x + long_seq[i:]
                        break
                    if (long_seq[len(long_seq)-i:] == x[:i]):
                        long_seq = long_seq + x[i:]
                        break
                    else:
                        if i < 20:
                            break



    if seq_list == []:
        break

print long_seq