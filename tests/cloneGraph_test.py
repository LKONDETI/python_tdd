#Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
#Output: [[2,4],[1,3],[2,4],[1,3]]

from unittest import TestCase
from src.katas.cloneGraph import Solution, Node  # Import Solution and Node

class TestCloneGraph(TestCase):
    
    def create_graph(self, adjList):
        """ Helper function to create a graph from the adjacency list """
        nodes = {}
        for i in range(len(adjList)):
            nodes[i + 1] = Node(i + 1)
        for i, neighbors in enumerate(adjList):
            nodes[i + 1].neighbors = [nodes[nei] for nei in neighbors]
        return nodes[1]  # Return the root node
    
    def graph_to_list(self, node):
        """ Helper function to convert graph to adjacency list format """
        result = []
        visited = set()
        
        def dfs(n):
            if n in visited:
                return
            visited.add(n)
            result.append([nei.val for nei in n.neighbors])
            for nei in n.neighbors:
                dfs(nei)
        
        dfs(node)
        return result
    
    def test_case1(self):
        adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
        expected = [[2, 4], [1, 3], [2, 4], [1, 3]]
        
        
        root_node = self.create_graph(adjList)
        
       
        cloned_graph = Solution().cloneGraph(root_node)
        
        
        self.assertEqual(self.graph_to_list(cloned_graph), expected)
    
    def test_single_node(self):
        adjList = [[]]
        expected = [[]]
        
       
        root_node = self.create_graph(adjList)
        
       
        cloned_graph = Solution().cloneGraph(root_node)
        
        
        self.assertEqual(self.graph_to_list(cloned_graph), expected)
    
    def test_empty_nodes(self):
        adjList = []
        expected = []
        
        # Create the graph from the adjacency list
        root_node = self.create_graph(adjList)
        
        # Clone the graph using the cloneGraph method
        cloned_graph = Solution().cloneGraph(root_node)
        
        # Convert the cloned graph to adjacency list and compare it with expected
        self.assertEqual(self.graph_to_list(cloned_graph), expected)
