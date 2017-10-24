def patterntonumber(st):
    d = {'A':0,'C':1,'G':2,'T':3}
    result = 0
    for k in range(len(st)):
        result = 4 * result + d[st[k]]
    return result

with open('rosalind_ba1l.txt') as f:
    i = 0
    string = ''
    for line in f:
        i += 1
        if i == 1:
            string = line.rstrip()

print(patterntonumber(string))


