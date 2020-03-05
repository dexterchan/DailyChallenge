from MyProject.TreeQueryCluster import Node, ClusterDependencyGraph, readTreeInput
import abc
JsonInput = "TreeQueryInput3.json"

# Demonstrate Postorder traversal of node tree for execution

from typing import List

class NodePipeline(abc.ABC):
    @abc.abstractmethod
    def addNodeToPipeline(self, parentNode:Node, node:Node):
        pass
    def retrieveCachedResult(self, identifier):
        pass

class CacheNode(Node):
    def __init__(self, node:Node):
        Node.__init__(self, node.description, node.action, node.cluster)
        self.originalNode = node


class DummyNodePipeline(NodePipeline):
    def __init__(self, cluster):
        self.Graph = {}
        self.cluster = cluster
    def addNodeToPipeline(self, parentNode:Node, node: Node):
        pass

    def retrieveCachedResult(self, identifier):
        pass





class NodeExecutor:


    def postOrderTraversalExecution(self, root:Node, jobList:List, nodePipeline: NodePipeline):
        parentCluster = root.cluster
        for child in root.children:
            if parentCluster == child.cluster:
                self.postOrderTraversalExecution(child, jobList, nodePipeline)
        jobList.append(root.description)
        return jobList


if __name__ == "__main__":
    rootNode = readTreeInput(JsonInput)
    #print (rootNode)

    clusterDepGraph = ClusterDependencyGraph()
    clusterDepGraph.constructDependencyGraph(rootNode)

    #Get workablecluster
    wList = clusterDepGraph.findClusterWithoutDependency()

    solu = NodeExecutor()

    step = 0
    while True:
        cnt = 0
        wList = clusterDepGraph.findClusterWithoutDependency()
        if len(wList) == 0:
            break
        print("step %d begin" % (step))
        print("\tTask List begin")
        for w in wList:
            nodePipeline = DummyNodePipeline(w.cluster)
            jobList = solu.postOrderTraversalExecution(w,[], nodePipeline)
            print("\t\t%d"%(cnt),jobList)
            node = clusterDepGraph.removeClusterDependency(w)
            cnt += 1
        print ("\tTask List end")
        print("step %d end" % (step))
        step += 1