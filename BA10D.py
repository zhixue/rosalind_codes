import itertools
def pairs(first, second):
    return [''.join(s) for s in itertools.product(first, second)]

def transformtable(data, states):
    transform_table = {}
    m = len(states)
    transitions = pairs(states, states) # ['AA','AB','BA','BB',.....]
    for i in range(m):
        values = map(float,data.readline().strip().split()[1:])
        for idx, value in enumerate(values):
            key = transitions[i * m + idx]
            transform_table[key] = value
    return transform_table

def emittable(data, states):
    emit_table = {}
    alphabet = ['x', 'y', 'z']
    m = len(states)
    emissions = pairs(states, alphabet) #['Ax','Ay','Az',....]
    for i in range(m):
        values = map(float, data.readline().strip().split()[1:])
        for idx, value in enumerate(values):
            key = emissions[i * len(alphabet) + idx]
            emit_table[key] = value
    return emit_table

def likelihood(string, transition_table, emission_table, states):
    transitions = pairs(states, states)
    n = len(string)
    m = len(states)
    # init
    p = [[0 for j in range(m)] for i in range(n)]
    for j in range(m):
        p[0][j] = emission_table[states[j] + string[0]] / m

    # start compute
    for i in range(1, n):   # the length of string xyzzxxyyyz...
        for j in range(m):  # the length of states A,B,C,D.....
            em_prob = emission_table[states[j] + string[i]]
            for x in range(m):  # sum the prob of former different states
                key = transitions[x * m + j]
                p[i][j] += p[i - 1][x] * transition_table[key] * em_prob
    prob = sum(p[-1])
    return prob

def skip(data, lines):
    for _ in range(lines):
        data.readline()

with open('rosalind_ba10d.txt') as f:
    path = f.readline().strip() # observed path
    skip(f, 3)  # only x,y,z
    states = f.readline().strip().split()    # maybe [A,B(,C,D)]
    skip(f, 2)
    transform_table = transformtable(f, states) # states transfrom matrix
    skip(f, 2)
    emit_table = emittable(f, states)   # emit possbility matrix
    prob = likelihood(path, transform_table, emit_table, states)    # compute the possbility
    print(prob)