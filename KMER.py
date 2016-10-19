
import itertools
def fun(a,b=4):
    li_4 = []
    for m in [''.join(m) for m in itertools.product(*[a] * b)]:
         li_4.append(m)
    return li_4
mer4 =  fun(['A','C','G','T'])

stseq = ''
for line in open('rosalind_kmer.txt'):
    if line[0] != '>':
        stseq = stseq + line.strip('\n')

mer4_count = [0]*4**4
for i in range(3,len(stseq)):
   for j in range(0,4**4):
       if stseq[i-3:i+1] == mer4[j]:
           mer4_count[j] += 1
for k in range(0,4**4):
    print mer4_count[k],