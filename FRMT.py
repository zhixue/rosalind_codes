from Bio import Entrez
from Bio import SeqIO

with open('rosalind_frmt.txt') as f:
    for line in f:
        ids = line.rstrip().split()

Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=ids, rettype="fasta")

records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format


min = 100000
flag = ''

for one in records:
    if len(one.seq)< min:
        min = len(one.seq)
        flag = one

print('>'+one.description)

st = one.seq
for k in range(len(st)):
    print(st[k],end='')
    if (k+1) % 70 == 0:
        print('')
