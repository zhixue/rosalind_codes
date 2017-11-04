def dfs(graph,node):
    visited = set()
    search(graph,node,visited)
    return visited

def search(graph,node,visited):
    visited.add(node)
    for theedge in graph.keys():
        if theedge[0] == node:
            if theedge[1] not in visited:
                search(graph,theedge[1],visited)

def cte(graph,specialedge):
    # the distance from the end node 'e' to start node 's' of the special edge , Bellman_Ford
    s,e = specialedge[0],specialedge[1]
    downnodes = dfs(graph,specialedge[1])
    if s not in downnodes:
        return -1
    # init
    d = {}
    inf = 1000000000000
    for node in downnodes:
        d[node] = graph[(e,node)] if (e,node) in graph else inf
    # compute
    for m in range(len(downnodes)):
        for edge in graph.keys():
            if edge[0] in downnodes and edge[1] in downnodes:
                # relax
                if d[edge[1]] > d[edge[0]] + graph[edge]:
                    d[edge[1]] = d[edge[0]] + graph[edge]
    return d[s] + graph[specialedge]

with open('rosalind_cte.txt') as f:
    graphlist = []
    edge = {}
    for line in f:
        if len(line.rstrip().split(' '))==2:
            nodenum=int(line.rstrip().split(' ')[0])
            if edge != {}:
                graphlist.append((edge,firstedge))
            edge = {}
        elif len(line.rstrip().split(' '))==3:
            start, end, length = line.rstrip().split(' ')
            if edge == {}:
                firstedge = (start,end)
            edge[(start,end)] = int(length)
    graphlist.append((edge,firstedge))

for one in graphlist:
    print(cte(*one),end=' ')