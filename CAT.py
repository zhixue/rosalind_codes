def fun(x):
    if x == 0:
        return 1
    else:
        return fun(x-1)*(4*x-2)/(x+1)
seq = ''
for line in open('rosalind_cat.txt'):
    if line[0] != '>':
        seq += line.rstrip()
cg_n = seq.count('C')
au_n = seq.count('A')

print (fun(cg_n)*fun(au_n))%1000000
