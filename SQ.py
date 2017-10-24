from collections import defaultdict
from itertools import combinations


def cycle_length_four(edges):
    '''Returns 1 if a square (cycle of length 4) is found, -1 otherwise.'''
    # Build a dictionary storing the neighbors of each node.
    neighbors = defaultdict(list)
    for n1, n2 in edges:
        neighbors[n1].append(n2)
        neighbors[n2].append(n1)

    # Store all neighbor pairs, looking for matching neighbor pairs.
    neighbor_pairs = set()
    for node in neighbors:
        # Iterate over all neighbor pairs for the give nodes.
        for n1, n2 in combinations(neighbors[node], 2):
            # If we've already found the neighbor pair once, we've got a square!
            if (n1,n2) in neighbor_pairs:
                #print(neighbor_pairs)
                return 1
            # If not, add the neighbor pairs to the set.
            else:
                neighbor_pairs.add((n1,n2))

    # No squares if we don't find any matching neighbor pairs.
    return -1


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('rosalind_sq.txt') as input_data:
        input_data.readline()  # Ignore first two lines.
        input_data.readline()
        edge_lists = [edges.split('\n') for edges in input_data.read().strip().split('\n\n')]
        edge_lists = [[map(int, nodes.split()) for nodes in edges[1:]] for edges in edge_lists]

    # Check each graph for a cycle of length four.
    squares = map(str, map(cycle_length_four, edge_lists))

    # Print and save the answer.

    print(' '.join(squares))

if __name__ == '__main__':
    main()