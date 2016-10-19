seq = ''
for line in open('rosalind_kmp.txt'):
    if line[0] != '>':
        seq += line.rstrip()
seq = ' '+seq
print 0,

for k in range(2,len(seq)):
    for length in range(min(k-1,20),0,-1):

        if seq[k-length+1:k+1] == seq[1:1+length]:
            print length,
            if length == 20:
                print '\n'
            break
        if length == 1:
            print 0,
