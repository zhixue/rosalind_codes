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

with open('rosalind_ba5n.txt') as f:
    file = f.readlines()
    edge = {}
    node = set()
    #nodenum,edgenum = file[0].rstrip().split(' ')
    for line in file[:]:
        start = line.rstrip().split(' ')[0]
        if start not in edge:
            edge[start] = []
            node.add(start)
        ends = line.rstrip().split('->')[-1][1:].split(',')

        for end in ends:
            edge[start].append(end)
            node.add(end)

    out = ''
    while(indegree_node(edge)!=[]):
        if len(indegree_node(edge)) > 1:
            out += ', ' + ', '.join(indegree_node(edge))
        else:
            out += ', ' + indegree_node(edge)[0]
        for one in indegree_node(edge):
            edge.pop(one)
            node.remove(one)

    for one in sorted(list(node)):
        out += ', ' + one

    print(out[2:])
