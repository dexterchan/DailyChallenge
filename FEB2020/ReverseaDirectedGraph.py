#Skill: Graph, map
#Given a directed graph, reverse the directed graph so all directed edges are reversed.

#Example:
#Input:
#A -> B, B -> C, A ->C

#Output:
#B->A, C -> B, C -> A
#Here's a starting point:

#Analysis
#from the graph structure
# iterate each node adj
# for each adj element, e.g. A->B insert MAP[B].append(A), where M is default map with element as list O(N)
# after all iteration
# re-create the graph from the default map
# iterate default MAP element
# clear the adjacent
# iterate the list of default map to re-create adjacent


from collections import defaultdict

class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value

def reverse_graph(graph):
    # Fill this in.
    M = defaultdict(list)
    for _, node in graph.items():
        l = node.adjacent
        v = node.value
        prevL = M[node]
        for kNode in l:
            M[kNode].append(v)
    newG = {}
    for k, v in M.items():
        k.adjacent = []
        for newAdj in v:
            k.adjacent.append(newAdj)
        newG[k.value] = k
    return newG


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')

    a.adjacent += [b, c]
    b.adjacent += [c]

    graph = {
        a.value: a,
        b.value: b,
        c.value: c,
    }

    for k, val in reverse_graph(graph).items():
        print(k, val.adjacent)
    # []
    # ['a', 'b']
    # ['a']