graph = []
with open('rosalind_cc.txt') as f:
    ll = 0
    for line in f:
        ll += 1
        if ll == 1:
            n = int(line.rstrip().split(' ')[0])
            continue

        edge1 = line.rstrip().split(' ')[0]
        edge2 = line.rstrip().split(' ')[1]
        exist = -1
        tempi = -1
        i = 0
        while(i<len(graph)):
            if (edge1 in graph[i] or edge2 in graph[i]):
                graph[i][edge1] = 1
                graph[i][edge2] = 1
                exist += 1
                if exist == 1:
                    graph[i] = dict(graph[i],**graph[tempi])
                    graph.pop(tempi)
                tempi = i
            i += 1
        if exist == -1:
            graph.append({edge1:1,edge2:1})

    print(n-sum([len(dic) for dic in graph])+len(graph))
