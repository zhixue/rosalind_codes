import itertools
def fun(a,b):

    for m in [''.join(m) for m in itertools.product(*[a] * b)]:
        print m

string = 'EHNSTWY'
x = list(string)
y = 3
fun(x,y)