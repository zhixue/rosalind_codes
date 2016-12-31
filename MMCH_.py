from math import factorial
def p(n,k):
    return factorial(n)//factorial(n-k)

stseq = ''
for line in open('rosalind_mmch.txt'):
    if line[0] == '>':
        stname = line[1:-1]
        if stseq != '':
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')

aunum = [stseq.count(nucl) for nucl in 'AU']
gcnum = [stseq.count(nucl) for nucl in 'GC']
ans = p(max(aunum),min(aunum))*p(max(gcnum),min(gcnum))
print(str(ans))
