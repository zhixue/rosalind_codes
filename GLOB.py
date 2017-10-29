from Bio.SubsMat import MatrixInfo

def score_match(pair, matrix):
    if pair not in matrix:
        return matrix[(tuple(reversed(pair)))]
    else:
        return matrix[pair]

def editdis(a,b):
    score = [[0 for x in range(len(b) + 1)] for y in range(len(a) + 1)]
    x = [[0 for x in range(len(b) + 1)] for y in range(len(a) + 1)]
    for i in range(0, len(a) + 1):
        for j in range(0, len(b) + 1):
            if i == 0 or j == 0:
                x[i][j] = max(i, j)
                score[i][j] = -5*i-5*j
            else:
                x[i][j] = min(x[i - 1][j] + 1, x[i][j - 1] + 1, x[i - 1][j - 1] + ((0 if a[i - 1] == b[j - 1] else 1)))
                score[i][j] += max(score[i-1][j-1]+score_match((a[i-1],b[j-1]),matrix= MatrixInfo.blosum62),score[i-1][j]-5,score[i][j-1]-5)
    return x[len(a)][len(b)],score[len(a)][len(b)]


with open('rosalind_glob.txt') as f:
    i = 0
    a = []
    b = []
    for line in f:
        i += 1
        if line.startswith('>'):
            if a == []:
                a.append(line)
            else:
                b.append(line)
        else:
            if b == []:
                a.append(line.rstrip())
            else:
                b.append(line.rstrip())

seq1 = ''.join(a[1:])
seq2 = ''.join(b[1:])

print(editdis(seq1,seq2)[1])

