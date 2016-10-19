S = ''
s = 'GTTGACTGT'
index = 0
while(index<len(S)):
    n = S[index:].find(s)
    #print S[index:]
    if n>-1:
        index = index + n +1
        print index-1,
    else:
        break
