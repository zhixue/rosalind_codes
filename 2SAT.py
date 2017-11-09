import sys
sys.setrecursionlimit(10000) #递归深度这里设置为一万

def the2_sat(graph,reversegraph):
    scc = kosaraju(graph, reversegraph)[1]
    # check
    ans = {}
    for cc in scc:
        for i in cc:
            if str(0-int(i)) in cc:
                return '0'
            ans[i] = 1
            ans[str(0-int(i))] = 0
    return '1 ' + ' '.join(map(str,sorted([int(x) for x in ans if ans[x] == 1], key=abs)))

def kosaraju(graph,reversegraph):
    firstdfs_order = dfs(graph)[0][::-1]
    return dfs(reversegraph, firstdfs_order)

def dfs(graph,sources = None):
    if sources == None:sources = sorted(graph.keys())
    visited = set()
    trees = []
    order = []
    for source in sources:
        if source not in visited:
            tree = []
            search(graph,visited,order,tree,source)
            trees.append(tree)
    return order,trees

def search(graph,visited,order,tree,fromnode):
    visited.add(fromnode)
    for adjnode in graph[fromnode]:
        if adjnode not in visited:
            search(graph,visited,order,tree,adjnode)
    order.append(fromnode)
    tree.append(fromnode)

with open('rosalind_2sat.txt') as f:
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

            nodenum.append(line.rstrip().split(' ')[0])
            edge = {}
            reverseedge = {}
            for n in range(1,int(line.rstrip().split(' ')[0])+1):
                edge[str(n)] = []
                edge['-'+str(n)] = []
                reverseedge[str(n)] = []
                reverseedge['-'+str(n)] = []
            tempedgenum = int(line.rstrip().split(' ')[1])
            countedge = 0
            edgeflag = True
        elif len(line.rstrip().split(' ')) == 2 and edgeflag == True:
            start, end = line.rstrip().split(' ')
            reversestart,reverseend = [str(0-int(x)) for x in (start,end)]
            if end not in edge[reversestart]:
                edge[reversestart].append(end)
            if start not in edge[reverseend]:
                edge[reverseend].append(start)
            if reverseend not in reverseedge[start]:
                reverseedge[start].append(reverseend)
            if reversestart not in reverseedge[end]:
                reverseedge[end].append(reversestart)

            countedge += 1
            if countedge == tempedgenum:
                edgeflag = False
    graphlist.append((edge,reverseedge))

for one in graphlist:
    print(the2_sat(*one))