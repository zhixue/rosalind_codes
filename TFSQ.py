with open('rosalind_tfsq.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i % 4 == 1:
            print('>'+line.rstrip()[1:])
        if i % 4 == 2:
            print(line.rstrip())
