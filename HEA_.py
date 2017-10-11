def Heapify(a, start, end):
    left = 0
    right = 0
    maxv = 0
    left = start * 2
    right = start * 2 + 1
    while left <= end:
        maxv = left
        if right <= end:
            if a[left] < a[right]:
                maxv = right
            else:
                maxv = left
        if a[start] < a[maxv]:
            a[maxv], a[start] = a[start], a[maxv]
            start = maxv
        else:
            break
        left = start * 2
        right = start * 2 + 1


def BuildHeap(a):
    size = len(a)
    i = (size - 1) // 2;
    while i >= 0:
        Heapify(a, i, size - 1)
        i = i - 1
    return ' '.join([str(x) for x in a])

with open('rosalind_test.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            print(BuildHeap([int(x) for x in line.rstrip().split(' ')]))