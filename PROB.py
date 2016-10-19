from math import log10
prob = []
seq = ''
for line in open('rosalind_prob.txt'):
    if line[0].isdigit():
        prob = line.split(' ')
    else:
        seq = line.strip('\n')

cg_content = (seq.count('C')+seq.count('G'))*1.0/len(seq)

for one in prob:
    one = float(one)
    print len(seq)*(cg_content*log10(one/2)+(1-cg_content)*log10((1-one)/2)),