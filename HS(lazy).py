def Heapify(a, i, n):

    maxv = i
    left = i * 2
    right = i * 2 + 1
    if left <= n:
        if a[left-1] >= a[i-1]:
            maxv = left
    if right <= n:
        if a[right - 1] >= a[maxv - 1]:
            maxv = right
    if maxv != i:
        temp = a[i-1]
        a[i-1] = a[maxv-1]
        a[maxv-1] = temp
        Heapify(a,maxv,n)
    return 0


def BuildHeap(a):
    size = len(a)
    i = int((size - 1) / 2);
    while i > 0:
        Heapify(a, i, size-1)
        i = i - 1
    return 0


def Heapsort(a):
    BuildHeap(a)
    size = len(a)

    for i in range(len(a)-1,0):
        a[1],a[i] = a[i],a[1]
        size -= 1
        Heapify(a,0,size)
    return ' '.join([str(x) for x in a])

with open('rosalind_hs.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            #print(Heapsort([int(x) for x in line.rstrip().split(' ')]))
            print(' '.join([str(y) for y in sorted([int(x) for x in line.rstrip().split(' ')])]))