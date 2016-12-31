from collections import Counter
i = 1
for line in open('rosalind_conv.txt'):
    if i == 1:
        S1 = [float(x) for x in line.rstrip().split(' ')]
    if i == 2:
        S2 = [float(x) for x in line.rstrip().split(' ')]
    i += 1

S_diff = []
for s1 in S1:
    for s2 in S2:
        S_diff.append(round(s1-s2,5))

print(Counter(S_diff).most_common(1))