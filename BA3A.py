with open('rosalind_ba3a.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            kmer = int(line.rstrip())
        if i == 2:
            string = line.rstrip()

with open('ba3a_out.txt','w') as fp:
    out = ''
    for n in range(len(string)-kmer+1):
        out += string[n:n+kmer] + '\n'
    out = out[:-1]
    fp.write(out)
