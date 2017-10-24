with open('rosalind_test.txt') as f:
    i = 0
    quickpass = False
    for line in f:
        i += 1
        if i == 1 or (quickpass == True and not line.startswith('\n')):
            continue
        if line.startswith('\n'):
            if quickpass == False and i != 2:
                print('1',end=' ')
            quickpass = False
            graph = [set(), set()]
            existnode = set()
            node,edge = 0,0

        if node == 0 and edge == 0 and len(line) > 1:
            node = int(line.rstrip().split(' ')[0])
            edge = int(line.rstrip().split(' ')[1])
        if node != 0:
            temp1 = int(line.rstrip().split(' ')[0])
            temp2 = int(line.rstrip().split(' ')[1])
            if (temp1 not in existnode) and (temp2 not in existnode):
                existnode.add(temp1)
                existnode.add(temp2)
                graph[0].add(temp1)
                graph[1].add(temp2)
            elif temp1 in existnode or temp2 in existnode:
                if temp1 in graph[0] and temp2 in graph[0]:
                    print('-1',end=' ')
                    quickpass = True
                elif temp1 in graph[1] and temp2 in graph[1]:
                    print('-1',end=' ')
                    quickpass = True
                elif temp1 in graph[0]:
                    existnode.add(temp2)
                    graph[1].add(temp2)
                elif temp1 in graph[1]:
                    existnode.add(temp2)
                    graph[0].add(temp2)
                elif temp2 in graph[0]:
                    existnode.add(temp1)
                    graph[1].add(temp1)
                elif temp2 in graph[1]:
                    existnode.add(temp1)
                    graph[0].add(temp1)
    if quickpass == False and node != 0:
        print('1', end=' ')