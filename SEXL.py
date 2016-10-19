def fun(dt):
    re_dt = []
    for one in dt:
        re_dt.append(str(2*(one-one**2)))
    return re_dt

for line in open('rosalind_sexl.txt'):
    data = line.rstrip().split(' ')
data = [float(x) for x in data]
print ' '.join(fun(data))