'''
 Time complex : O(n^2)


counter = 0

with open('rosalind_inv.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            numbers = [int(x) for x in line.strip().split(' ')]

for m in range(len(numbers)):
    for n in range(m+1,len(numbers)):
        if numbers[m] > numbers[n]:
            counter += 1

print(counter)
'''
def SortCount(A):
   l = len(A)
   if l > 1:
      n = l//2
      C = A[:n]
      D = A[n:]
      C, c = SortCount(A[:n])
      D, d = SortCount(A[n:])
      B, b = MergeCount(C,D)
      return B, b+c+d
   else:
      return A, 0


def MergeCount(A,B):
   count = 0
   M = []
   while A and B:
      if A[0] <= B[0]:
         M.append(A.pop(0))
      else:
         count += len(A)
         M.append(B.pop(0))
   M  += A + B
   return M, count


with open('rosalind_inv.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 2:
            numbers = [int(x) for x in line.strip().split(' ')]

print(SortCount(numbers)[1])