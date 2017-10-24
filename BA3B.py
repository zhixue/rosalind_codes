with open('rosalind_ba3b.txt') as f:
    i = 0
    out = ''
    for line in f:
        i += 1
        if i == 1:
            out = line.rstrip()
        else:
            out += line.rstrip()[-1]

    print(out)
