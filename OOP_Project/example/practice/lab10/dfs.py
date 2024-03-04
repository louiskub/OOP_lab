from collections import defaultdict

class Graph: 
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        if u not in self.graph.keys() :
            self.graph[u] = []
        if v not in self.graph.keys() :
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, u, visited) :

        visited.add(u)
        print(u, end=" ")

        if u not in self.graph.keys() :
            return None
        for next in self.graph[u] :
            if next not in visited:
                self.dfs_recursive(next, visited)

    def dfs(self, u):
        visited = {u}
        stack = [u]

        while stack != []:
            now = stack.pop()
            print(now, end=" ")

            if now not in self.graph.keys() :
                continue
            for next in self.graph[now] :
                if next not in visited :
                    visited.add(next)
                    stack.append(next)

    def bfs(self, u):
        
        visited = {u}
        queue = [u]

        while queue != []:
            now = queue.pop(0)
            print(now, end=" ")

            if now not in self.graph.keys() :
                continue
            for next in self.graph[now] :
                if next not in visited :
                    visited.add(next)
                    queue.append(next)


g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(4, 8)
g.addEdge(4, 9)
g.addEdge(5, 10)
g.addEdge(5, 11)
g.addEdge(6, 12)
g.addEdge(6, 13)

print("Following is Depth First Traversal (starting from vertex 2)")
    
# Function call
g.dfs_recursive(1, set())
print("")
g.dfs(1)
print("")
g.bfs(1)
