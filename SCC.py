def kosaraju(matrix):
    return dfs(reversed_edgematrix, dfs(edge_matrix)[0][::-1])[1]

def dfs(matrix,sources = None):
    if sources == None:sources = range(len(matrix))
    visited = [-1 for j in range(len(matrix))]
    tree_num = 0
    order = []
    for source in sources:
        if visited[source] == -1:
            tree_num += 1
            search(matrix,visited,order,source)
    return order,tree_num

def search(matrix,visited,order,fromnode):
    visited[fromnode] = 1
    for adjnode in range(len(matrix[fromnode])):
        if visited[adjnode] == -1 and matrix[fromnode][adjnode] == 1:
            search(matrix,visited,order,adjnode)
    order.append(fromnode)

with open('rosalind_scc.txt') as f:
    nodenum,edgenum = map(int,f.readline().rstrip().split(' '))
    edges = f.readlines()
    edge_matrix = [[-1 for i in range(nodenum)] for j in range(nodenum)]
    reversed_edgematrix = [[-1 for i in range(nodenum)] for j in range(nodenum)]
    for edge in edges:
        start,end = map(int,edge.rstrip().split(' '))
        edge_matrix[start-1][end-1] = 1
        reversed_edgematrix[end-1][start-1] = 1

print(kosaraju(edge_matrix))