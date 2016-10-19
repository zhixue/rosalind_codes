def dichotomy(L,K,Index):
    if L.count(k) == 0:
        return -2
    if(len(L) == 1):
        return Index

    length = len(L) / 2
    hit = L[length]

    if(hit == K):
        return Index + length
    else:
        if hit > K:
            return dichotomy(L[:length],K,Index)
        else:
            return dichotomy(L[length + 1:],K,Index + length + 1)



if __name__ == '__main__':
    l = 0
    for line in open('rosalind_bins.txt'):
        l += 1
        if l == 3:
            L = [int(x) for x in line.rstrip().split(' ')]
        if l == 4:
            K = [int(x) for x in line.rstrip().split(' ')]

    for k in K:
        index = dichotomy(L,k,0)
        print index+1,