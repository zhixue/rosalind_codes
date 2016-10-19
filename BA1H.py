l = 0
for line in open('rosalind_ba1h.txt'):
    l += 1
    if l == 1:
        pattern = line.rstrip()
    if l == 2:
        string = line.rstrip()
    if l == 3:
        k = int(line.rstrip())
n = len(pattern)
for i in range(len(string)-n):
    sub_s = string[i:i+n]
    mis = 0
    for j in range(n):
        if sub_s[j] != pattern[j]:
            mis += 1
        if mis > k:
            break
        if j == n-1:
            print i,
