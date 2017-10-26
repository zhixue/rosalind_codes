inf = 1000000000 # large number as Inf

def mindistance(edgematrix,start = 0):
    # init single source
    d = [inf for n in range(len(edgematrix))] # the distance from start to other nodes
    d[start] = 0
    unvisited = set(range(len(edgematrix)))

    # Dijkstra - o(n^2)
    while unvisited:
        mindis = inf
        for j in unvisited:
            if( d[j] <= mindis):
                u = j
                mindis = d[j]
        unvisited.remove(u)

        for k in range(len(edgematrix)):
            if(d[k]>d[u]+edgematrix[u][k] and edgematrix[u][k]>0):
                # relax
                d[k] = d[u] + edgematrix[u][k]
    return d

''''
    # Floyd - o(n^3)
    dismatrix = edgematrix
    for i in range(len(edgematrix)):
        for j in range(len(edgematrix)):
            for k in range(len(edgematrix)):
                init_dis = dismatrix[j][i]+dismatrix[i][k]
                if(dismatrix[j][k]>init_dis):
                    dismatrix[j][k] = init_dis
    return dismatrix
'''

with open('rosalind_dij.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            nodenum = int(line.rstrip().split()[0])
            edgematrix = [[-1 for i in range(nodenum)] for j in range(nodenum)]

        else:
            temp = line.rstrip().split()
            start = int(temp[0])
            end = int(temp[1])
            length = int(temp[2])

            edgematrix[start-1][end-1] = length
            for i in range(len(edgematrix)):
                edgematrix[i][i] = 0

string = ' '.join([str(x) for x in mindistance(edgematrix)]).replace('1000000000','-1')

with open('out_dij.txt','w') as f:
    f.write(string)

print(string)   # upload the file will be correct but filling the blank will be wrong


