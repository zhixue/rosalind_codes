def indegree_node(inputs):
    thegraph, nodes = inputs
    # init
    result = '1'
    # search indgree = 0
    while(thegraph!={}):
        out_nodes = []
        for one in nodes.keys():
            if nodes[one] == 0:
                out_nodes.append(one)
        if len(out_nodes) > 1:
            return '-1'
        else:
            # delete the node and change the hash
            result += ' ' + out_nodes[0]
            thegraph,nodes = update(thegraph,nodes,out_nodes[0])
    if len(nodes) > 1:
        return '-1'
    else:
        return result + ' ' + str(*nodes)

def update(thegraph,nodes,out_node):
    for downstream in thegraph[out_node]:
        nodes[downstream] -= 1
    thegraph.pop(out_node)
    nodes.pop(out_node)
    return thegraph,nodes

with open('rosalind_hdag.txt') as f:
    graphlist = []
    edge = {}
    edgeflag = False
    nodenum = []
    for line in f:
        if line.startswith('\n'):
            continue
        elif len(line.rstrip().split(' ')) == 2 and edgeflag == False:
            if edge != {}:
                graphlist.append((edge, node))
                edgeflag = False
            edge = {}  # start:ends
            node = {}   # node:indegreenum
            nodenum.append(line.rstrip().split(' ')[0])
            tempedgenum = int(line.rstrip().split(' ')[1])
            countedge = 0
            edgeflag = True
        elif len(line.rstrip().split(' ')) == 2 and edgeflag == True:
            start, end = line.rstrip().split(' ')
            if start not in edge:
                edge[start] = []
            edge[start].append(end)
            if end not in node:
                node[end] = 0
            if start not in node:
                node[start] = 0
            node[end] += 1
            countedge += 1
            if countedge == tempedgenum:
                edgeflag = False
    graphlist.append((edge,node))

print('\n'.join(map(indegree_node,graphlist)))