def compute_pro(string,probs):
    d = {'A':0,'C':1,'G':2,'T':3}
    result = 1
    for k in range(len(string)):
        result += probs[d[string[k]]][k]
    return result


with open('rosalind_ba2c.txt') as input_data:
    seq = input_data.readline().strip()
    length = int(input_data.readline())
    probs = [map(float, line.strip().split()) for line in input_data.readlines()]



probs = [list(x) for x in probs]

maxprob = 0
maxstring = ''
for n in range(len(seq)-length+1):
    temp = seq[n:n+length]
    tempprob = compute_pro(temp,probs)
    if tempprob > maxprob:
        maxstring = temp
        maxprob = tempprob


print(maxstring)
