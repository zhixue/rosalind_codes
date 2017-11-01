import time
c = time.time()
def find_triples(array,ln):
    arrayindex = {}
    for k in range(ln):
        if array[k] not in arrayindex:
            arrayindex[array[k]] = set()
        arrayindex[array[k]].add(k)

    for m in range(ln):
        for n in range(m+1,ln):
            sum2 = -array[m]-array[n]
            if sum2 in arrayindex:
                pro_index = filter(lambda x:x!=m and x!=n,arrayindex[sum2])
                return m,n,tuple(pro_index)[0]

def solve(array):
    length = len(array)
    result = find_triples(array, length)
    if result:
        return ' '.join(map(lambda x: str(x + 1), result))
    else:
        return '-1'

with open('rosalind_3sum.txt') as f:
        times,length = map(int, f.readline().split())
        l_array = [tuple(map(int, f.readline().split())) for time in range(times)]
        print('\n'.join(list(map(solve,l_array))))

print("\nCost time is %s seconds" %str(time.time()-c))