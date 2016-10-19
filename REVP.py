string = ''
for line in open('rosalind_revp.txt'):
    if line[0]!='>':
        string = string + line.strip('\n')


for start in range(0,len(string)-2):
    maxle = min(14,len(string)-start)
    if maxle <= 4:
        maxle = 6

    for length in range(4,maxle,2):
        reverse_seq = string[start:start+length]

        #print reverse_seq
        for i in range(length):
            if (reverse_seq[i]=='A' and reverse_seq[-1-i]=='T') \
            or (reverse_seq[i]=='T' and reverse_seq[-1-i]=='A')\
            or (reverse_seq[i]=='C' and reverse_seq[-1-i]=='G') \
            or (reverse_seq[i]=='G' and reverse_seq[-1-i]=='C'):
                if i == length/2:
                    print start+1,length
                    break
            else:
                break