from numpy import zeros,arange
def longest_common_subsequence(lhs,rhs):
    l_len = len(lhs);
    r_len = len(rhs);
    matrix = zeros((l_len,r_len))
    for i in arange(l_len):
        for j in arange(r_len):
            if lhs[i] == rhs[j]:
                if i != 0 and j != 0:
                    matrix[i][j] = matrix[i-1][j-1]+1
                else:
                    matrix[i][j] = 1
            elif i != 0 and j != 0:
                    matrix[i][j] = max(matrix[i-1][j],matrix[i][j-1])
    return matrix

def print_longest_common_subsequence(lhs,rhs):
    matrix = longest_common_subsequence(lhs,rhs)
    l_len = len(lhs)
    r_len = len(rhs)
    i = l_len-1
    j=r_len-1
    rst = [];
    while j>0 and i >0:
        if matrix[i-1][j] != matrix[i][j] and matrix[i][j-1] != matrix[i][j]:
            rst. insert(0,lhs[i])
            #print(i,j);
            j = j-1
            i = i-1
        elif matrix[i-1][j] == matrix[i][j]:
            i = i-1
        else:
            j=j-1
    if j!=0 and i== 0:
        if matrix[i][j-1] != matrix[i][j]:
            rst. insert(0,lhs[i])
    elif j==0 and 0:
        if matrix[i][j] != matrix[i-1][j]:
            rst. insert(0,lhs[j])
    return rst

i = 0
string1 = ' '
string2 = ' '
for line in open('rosalind_lcsq.txt'):
    if line[0] != '>':
        if i == 1:
            string1 += line.rstrip()
        else:
            string2 += line.rstrip()
    else:
        i += 1

print len(string1),len(string2)
print ''.join(print_longest_common_subsequence(string1,string2))