from itertools import product
def trans(refa,a):
    result = []
    for j in range(len(a)):
        for i in range(len(refa)):
            if a[j] == refa[i]:
                result.append(i)
    return result

def reverselist(array,i,j):
    return array[:i] + array[i:j+1][::-1] + array[j+1:]

def breakpointfind(x, y):   # breakpoint: the numbers are not adjacent
    return abs(x - y) != 1

def breakpointcount(permutation):   # add 0 and length+1 to make it easy to count breakpoint
    permutation = [0] + list(permutation) + [len(permutation) + 1]
    return sum(map(breakpointfind, permutation[1:], permutation[:-1]))

def breakpointindice(permutation):  # the list of breakpoint index
    permutation = [0] + list(permutation) + [len(permutation) + 1]
    breakpoint_indice = []
    for idx in range(len(permutation)-1):
        if breakpointfind(permutation[idx],permutation[idx+1]):
            breakpoint_indice.append(idx)
    return breakpoint_indice

def reverse_distance(a1, a2):
    if a1 == a2:
        return 0
    # init
    indices = []
    for number in a1:
        for idx in a2:
            if a2[idx] == number:
                indices.append(idx+1)
    current_p = {tuple(indices):[]}
    min_breaks = breakpointcount(indices)
    dist = 0
    while True: # start
        new_p = {} # new_p is a dict of indices:traces with min breakpoints
        dist += 1
        if dist > len(a1):  # avoid can't be solved
            return -1
        for p in current_p.keys():
            for start,endplus in product(breakpointindice(p), repeat=2):
                temp_perm = tuple(reverselist(p, start, endplus-1))
                temp_breaks = breakpointcount(temp_perm)
                temp_trace = current_p[p]+[(start+1,endplus)]
                if temp_breaks == 0:
                    return dist,temp_trace
                if temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_p = {temp_perm:temp_trace} # init the new_p
                elif temp_breaks == min_breaks:
                    new_p[temp_perm] = temp_trace
        current_p = new_p

with open('rosalind_sort.txt') as f:
    i = 0
    old = []
    new = []
    for line in f:
        i += 1
        if i % 3 == 1:
            old = [int(x) for x in line.rstrip().split(' ')]
        if i % 3 == 2:
            new = [int(x) for x in line.rstrip().split(' ')]
            dis,rs = reverse_distance(list(range(10)), trans(old, new))
            print(dis)
            for one in rs:
                print(' '.join([str(x) for x in one]))