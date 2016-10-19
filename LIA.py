import itertools
def f(k,n):
    p = []
    child_num = 2**k
    for i in range(n):
        p.append(len(list(itertools.combinations([x for x in range(child_num)],i)))*(0.25**i)*(0.75**(child_num-i)))

    return 1-sum(p)

print f(5,8)