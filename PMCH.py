import math
stseq = ''
for line in open('rosalind_pmch.txt'):
    if line[0] == '>':
        if stseq != '':
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')

n1 = stseq.count('A')
n2 = len(stseq)/2 - n1
print math.factorial(n1)*math.factorial(n2)
