sa = raw_input('string1')
sb = raw_input('string2')
c = 0
for i in range(len(sa)):
    if sa[i] != sb[i]:
        c = c + 1
print c