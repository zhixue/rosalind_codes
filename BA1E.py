def fun(s,k,l,t):
    n = len(s)
    result = []
    for i in range(n-l):
        sub_s = s[i:i+l]
        for j in range(l-k):
            if sub_s.count(sub_s[j:j+k]) >= t:
                result.append(sub_s[j:j+k])
    result = [x for x in set(result)]
    return result
'''
def count(S,s):
    count = 0
    for l in range(len(S)-len(s)):
        if S[l:l+len(s)] == s:
            count += 1
    return count
'''



stri=''
print ' '.join(fun(stri,10,597,17))
