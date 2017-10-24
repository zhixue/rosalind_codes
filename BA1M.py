def numbertopattern(num,lth):
    reversestring = ''
    l = ['A','C','G','T']
    for i in range(lth):
        res = int(num % 4)
        reversestring += l[res]
        num = (num - res)/4
    return reversestring[::-1]


with open('rosalind_ba1m.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            number = int(line.rstrip())
        if i == 2:
            length = int(line.rstrip())

print(numbertopattern(number,length))


