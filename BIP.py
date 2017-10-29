
def find_bool(graph):
    thisside = set('1')
    thatside = set()

    while(True):
        edges_count = sum([len(graph[node]) for node in graph.keys()])
        if edges_count == 0:
            break
        for start in graph.keys():
            if graph[start] == []:continue
            if start in thisside:
                thatside = thatside|set(graph[start])
                graph[start] = []
            elif start in thatside:
                thisside = thisside|set(graph[start])
                graph[start] = []

            if thisside&thatside != set():
                return -1
        if sum([len(graph[node]) for node in graph.keys()]) == edges_count:
            return 1
    return 1




with open('rosalind_bip.txt') as f:
    i = 0
    listgraph = []

    edge = {}
    for line in f:
        i += 1
        if i == 1:
            continue
        if line.startswith('\n'):
            line = next(f)
            temp = line.rstrip().split(' ')
            nodenum = int(temp[0])
            edgenum = int(temp[1])
            if not edge == {}:
                listgraph.append(edge)
            edge = {}

        else:
            temp = line.rstrip().split(' ')
            start = temp[0]
            end = temp[1]
            if start in edge:
                edge[start].append(end)
            else:
                edge[start] = [end]

            if end in edge:
                edge[end].append(start)
            else:
                edge[end] = [start]
listgraph.append(edge)

#print(listgraph)
for graph in listgraph:
    print(find_bool(graph),end=' ')

