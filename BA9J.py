def found(string,s,n):
    ct = 0
    for i in range(len(string)):
        if string[i] == s:
            ct += 1
        if ct == n:
            return i
    return -1


def ReBWT(Lst):
    length = len(Lst)
    result = [' ' for x in range(length)]
    Fst = ''.join(sorted([k for k in Lst]))

    pos = 0


    for num in range(length-1,-1,-1):
        result[num] = Lst[pos]

        pos = found(Fst,Lst[pos],Lst[:pos+1].count(Lst[pos]))


    return ''.join(result[1:])+'$'


with open('rosalind_ba9j.txt') as f:
    string = ''
    for line in f:
        string += line.rstrip()
    print(ReBWT(string))