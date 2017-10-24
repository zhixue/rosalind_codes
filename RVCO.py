from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open('rosalind_rvco.txt') as f:
    i = 0
    counter = 0
    dna = ''
    for line in f:

        if line.startswith('>'):
            if dna != '':
                my_seq = Seq(dna, IUPAC.unambiguous_dna)
                reversedna = str(my_seq.reverse_complement())
                if dna == reversedna:
                    counter += 1
            dna = ''
        else:
            dna += line.rstrip()

my_seq = Seq(dna, IUPAC.unambiguous_dna)
reversedna = str(my_seq.reverse_complement())
if dna == reversedna:
    counter += 1

print(counter)
