n_s_gc = []
stseq = ''
for line in open('rosalind_gc.txt'):
    if line[0] == '>':
        stname = line[1:-1]
        if stseq != '':
            gc_c = (stseq.count('G')+stseq.count('C'))*100.0/(stseq.count('G')+stseq.count('C')+stseq.count('T')+stseq.count('A'))
            n_s_gc.append([stname,gc_c])
            stseq = ''
    else:
        stseq = stseq + line.strip('\n')
gc_c = (stseq.count('G')+stseq.count('C'))*100.0/(stseq.count('G')+stseq.count('C')+stseq.count('T')+stseq.count('A'))
n_s_gc.append([stname,gc_c])
highest = ['',0]
for one in n_s_gc:
    if one[1] > highest[1]:
        highest = one
print highest[0],highest[1],'%'