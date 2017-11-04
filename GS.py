def boolgs(graph,numofnode):
    for node in graph.keys():
        if len(dfs(graph,node)) == int(numofnode):
            return node
    return '-1'

def dfs(graph,node):
    visited = set()
    search(graph,node,visited)
    return visited

def search(graph,node,visited):
    visited.add(node)
    if node in graph:
        for one in graph[node]:
            if one not in visited:
                search(graph,one,visited)

with open('rosalind_gs.txt') as f:
    graphlist = []
    edge = {}
    edgeflag = False
    nodenum = []
    for line in f:
        if line.startswith('\n'):
            continue
        elif len(line.rstrip().split(' ')) == 2 and edgeflag == False:
            if edge != {}:
                graphlist.append(edge)
                edgeflag = False
            edge = {}  # start:ends
            nodenum.append(line.rstrip().split(' ')[0])
            tempedgenum = int(line.rstrip().split(' ')[1])
            countedge = 0
            edgeflag = True
        elif len(line.rstrip().split(' ')) == 2 and edgeflag == True:
            start, end = line.rstrip().split(' ')
            if start not in edge:
                edge[start] = []
            edge[start].append(end)
            countedge += 1
            if countedge == tempedgenum:
                edgeflag = False
    graphlist.append(edge)

for m in range(len(graphlist)):
    print(boolgs(graphlist[m],nodenum[m]),end = ' ')