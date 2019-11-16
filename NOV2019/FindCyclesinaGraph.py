#Given an undirected graph, determine if a cycle exists in the graph.
from collections import deque
class Solution:
  def find_Cycle(self, graph):
    return self.__bfs(graph)

  def __bfs(self, g):
    visitedNode = set()
    __queue = deque()
    lvlnodes = self.__insertDict2StackHelper(g, __queue)
    self.__checkCyclic(visitedNode, lvlnodes)

    while len(__queue) > 0:
      subg = __queue.popleft()
      lvlnodes = self.__insertDict2StackHelper(subg, __queue)
      if self.__checkCyclic(visitedNode, lvlnodes):
        return True
    return False

  def __insertDict2StackHelper(self, g, q):
    levelNodes = set()
    for key in g.keys():
      levelNodes.add(key)
      q.append(g[key])
    return levelNodes

  def __checkCyclic(self, visitedNode, lvlNodes):
    intersect = visitedNode.intersection(lvlNodes)
    if(len(intersect)>0):
      return True
    for x in lvlNodes:
      visitedNode.add(x)
    return False



def find_cycle(graph):
  # Fill this in.
  solu = Solution()
  return solu.find_Cycle(graph)

if __name__ == "__main__":
  graph = {
    'a': {'a2':{}, 'a3':{} },
    'b': {'b2':{}},
    'c': {}
  }
  print (find_cycle(graph) )
  # False
  graph['c'] = graph
  print (find_cycle(graph) )
  # True