for line in open('rosalind_ba9d.txt'):
    stseq = line.rstrip()

for length in range(len(stseq)-1,1,-1):
    for start in range(0,len(stseq)-length):
        st = stseq[start:start+length]
        if stseq[start+1:].find(st) > 0 :
            print(st)
            break


