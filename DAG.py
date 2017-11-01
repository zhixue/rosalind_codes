def indegree_node(thegraph,indgree = 0):
    out_nodes = []
    for node1 in thegraph.keys():
        counter = 0
        for node2 in thegraph:
            if node1 in thegraph[node2]:
                counter += 1
        if counter == indgree:
            out_nodes.append(node1)
    return out_nodes

def acyclic(graph):
    nodenum = len(graph.keys())
    #delnum = 1000000
    sumdelnum = 0
    while(indegree_node(graph)!=[]):
        for one in indegree_node(graph):
            graph.pop(one)
            #delnum += 1
            sumdelnum += 1
    if nodenum == sumdelnum: return '1'
    else: return  '-1'

with open('rosalind_dag.txt') as f:
    i = 0
    listgraph = []
    edge = {}
    for line in f:
        i += 1
        if i == 1:
            continue
        elif line.startswith('\n'):
            line = next(f)
            nodenum,edgenum = line.rstrip().split(' ')
            if edge != {}:
                listgraph.append(edge)
            edge = {}
        else:
            start,end = line.rstrip().split(' ')
            if start not in edge:
                edge[start] = []
            edge[start].append(end)
    listgraph.append(edge)

print(' '.join(map(acyclic,listgraph)))