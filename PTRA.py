from Bio.Seq import translate
with open('rosalind_ptra.txt') as f:
    dna = f.readline().rstrip()
    prot = f.readline().rstrip()
for i in range(1,27):
    if i in(7,8,15,17,18,19,20):
        continue
    if translate(dna,table=i,to_stop=True) == prot:
        print(i)