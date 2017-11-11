def inout_degree_node(thegraph):
    inout_nodes = []
    for node1 in thegraph.keys():
        counter = 0
        for node2 in thegraph:
            if node1 in thegraph[node2]:
                counter += 1
        if counter != len(thegraph[node1]):
            inout_nodes.append(node1)
    return inout_nodes

def parse_data(data, mmap):
    for line in data:
        temp = line.split(" -> ")
        mmap[temp[0]] = temp[1].split(",")
    return mmap

def combine_cycles(cycle1, cycle2):
    temp = cycle2.split("->")
    temp.pop()
    temp2 = cycle1.split("->")
    location = temp2.index(temp[0])
    temp2[location] = "*****"
    blah = "->".join(temp2)
    location = blah.find("*****")

    return cycle1[:location] + "->".join(temp) + "->" + cycle1[location:]

def find_cycle(cycles, mmap, key):
    cycle = ""
    if key == "none":
        # find node that has open edges and set it as start
        for key in mmap.keys():
            if mmap[key]:
                cycle = key
                break

        # set key to cycle

        key = cycle
    else:
        cycle = key

    # walk through until there is no edge left
    while mmap[key]:
        cycle += "->"
        # always choose first from the list
        key = mmap[key].pop(0)
        cycle += key
    if cycles != "":
        cycles = combine_cycles(cycles, cycle)
    else:
        cycles = cycle
    return (cycles, mmap)

def find_y(cycles, mmap):
    temp = cycles.split("->")
    for node in temp:
        if mmap[node] != []:
            return node
    return "completed"


with open('rosalind_ba3h.txt') as f:
    ls = [x.rstrip() for x in f.readlines()][1:]
    kmers = [(line[:-1], line[1:]) for line in ls]
    mmap = {}
    nodes = set()
    for one in kmers:
        nodes.add(one[0])
        nodes.add(one[1])
        if one[0] not in mmap:
            mmap[one[0]] = []
        mmap[one[0]].append(one[1])


cycles = ""

st = inout_degree_node(mmap)
for one in st:
    if len(st) == 2:
        tempend = st[0]
        tempstart = st[1]    # 1/2 prob to be right!!!! but can be checked!
    else:
        if one in mmap.keys():
            tempend = one
            temp = nodes - set(mmap.keys())
            for one in temp:
                tempstart = one
'''
#print('temp add a edge:'+tempstart+'->'+tempend)
'''
mmap[tempstart] = [tempend]


# first run through to find main cycle
temp = find_cycle(cycles, mmap, "none")
cycles = temp[0]
mmap = temp[1]
nextone = find_y(cycles, mmap)


while nextone != "completed":
    temp = find_cycle(cycles, mmap, nextone)
    cycles = temp[0]
    mmap = temp[1]
    nextone = find_y(cycles, mmap)
cycles = cycles.split('->')[1:]

for i in range(len(cycles)-1):
    if cycles[i] == tempstart and cycles[i+1] == tempend:
        break
cycles = cycles[i+1:]+cycles[:i+1]

out = ''
for one in cycles:
    if out == '':
        out += one
    else:
        out += one[-1]
print(out)