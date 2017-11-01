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

with open('rosalind_ts.txt') as f:
    file = f.readlines()
    edge = {}
    node = set()
    nodenum,edgenum = file[0].rstrip().split(' ')
    for line in file[1:]:
        start,end = line.rstrip().split(' ')
        if start not in edge:
            edge[start] = []
            node.add(start)
        edge[start].append(end)
        node.add(end)

    while(indegree_node(edge)!=[]):
        print(*indegree_node(edge),end=' ')
        for one in indegree_node(edge):
            edge.pop(one)
            node.remove(one)
    print(*node)