def BWT(st):
    if st[-1] != '$':
        st += '$'
    length = len(st)
    temp = st + st
    rotate = [temp[k:k+length] for k in range(length)]
    return ''.join(map(lambda s:s[-1],sorted(rotate)))

with open('rosalind_ba9i.txt') as f:
    string = ''
    for line in f:
        string += line.rstrip()
    print(BWT(string))
