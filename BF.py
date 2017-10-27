inf = 100000000

def Bellman_Ford(edgelist,nodenum,start = 0):
    # init
    dist = [inf for i in range(nodenum)]
    dist[start] = 0
    for n in range(len(edgelist)):
        if edgelist[n][0] == start:
            dist[edgelist[n][1]] = edgelist[n][2]

    for m in range(nodenum-1):
        check = 0
        for n in range(len(edgelist)):
            # relax
            if(dist[edgelist[n][1]-1]>dist[edgelist[n][0]-1]+edgelist[n][2]):
                dist[edgelist[n][1]-1] = dist[edgelist[n][0]-1] + edgelist[n][2]
                check = 1


    flag = 0
    #  has the the circle of edge<0?
    for n in range(len(edgelist)):
        if (dist[edgelist[n][1]-1] > dist[edgelist[n][0]-1] + edgelist[n][2]):
            flag = 1
            break
        if flag == 1:
            return None
    return dist




with open('rosalind_bf.txt') as f:
    i = 0
    for line in f:
        i += 1
        if i == 1:
            nodenum = int(line.rstrip().split()[0])
            edgematrix = [[inf for i in range(nodenum)] for j in range(nodenum)]
            edgelist = [] # start,end,weight

        else:
            temp = line.rstrip().split()
            start = int(temp[0])
            end = int(temp[1])
            length = int(temp[2])

            edgelist.append([start,end,length])
            edgematrix[start-1][end-1] = length
            for i in range(len(edgematrix)):
                edgematrix[i][i] = 0

#print(edgelist)
for x in Bellman_Ford(edgelist,nodenum,0):
    if x > inf / 10:
        print('x',end = ' ')
    else:
        print(str(x),end = ' ')