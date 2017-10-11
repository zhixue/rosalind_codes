with open('rosalind_maj.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            count_list = [int(x) for x in line.rstrip().split(' ')]
            result = [-1 for x in range(count_list[0])]
        if i != 1:
            temp = [int(x) for x in line.rstrip().split(' ')]
            for one in temp:
                if temp.count(one) > count_list[1]/2:
                    result[i-2] = one
                    break

    print(' '.join([str(x) for x in result]))