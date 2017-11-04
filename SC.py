def boolsc(graph,reversegraph,numofnode):
    for node in graph.keys():
        if len(dfs(graph,node)|dfs(reversegraph,node))<int(numofnode):
            return -1
    return 1

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


with open('rosalind_sc.txt') as f:
    graphlist = []
    edge = {}
    reverseedge = {}
    edgeflag = False
    nodenum = []
    for line in f:
        if line.startswith('\n'):
            continue
        elif len(line.rstrip().split(' ')) == 2 and edgeflag == False:
            if edge != {}:
                graphlist.append((edge,reverseedge))
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
            if end not in reverseedge:
                edge[end] = []
            edge[end].append(start)
            countedge += 1
            if countedge == tempedgenum:
                edgeflag = False
    graphlist.append((edge,reverseedge))

for k in range(len(graphlist)):
    print(boolsc(graphlist[k][0],graphlist[k][1],nodenum[k]),end=' ')