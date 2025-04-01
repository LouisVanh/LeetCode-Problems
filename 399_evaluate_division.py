from typing import List
from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Pairs of equations[i] = ["a","b"]
        # equations[i][0] (a) / (b) equations[i][1] = values[i]
        # Thus, a = values[i] * b and b = 1/values[i] * a
        # This can be seen as a graph problem: let the edges between nodes be = the multiplier to get there.
        # going from a -> b -> c = edge(a,b) * edge(b,c)
        # so, use bfs to find the shortest path from a -> c for performance reasons (and to avoid cycles)
        # how do i find the actual edges between a and c, given that i've found c through bfs?
        # keep track of the total multiplier needed to actually get to the point we're at, store it with the node
        graph = defaultdict(list)

        for (a,b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1/value))

        def bfs(start, end):
            if(start not in graph or end not in graph):
                return -1.0 # Can't find it, even if it's x/x (in problem description...)
            
            if start == end:
                return 1.0 # They're the same node. Getting there is equivalent to *1
            
            queue = deque([(start, 1.0)]) # Deque is O(1) pop time, > list O(n)
            visited = set()

            # go over the stack,
            while queue:
                node, val = queue.popleft()
                if(node == end):
                    return val
                if(node in visited): continue # already went here, exit out early

                visited.add(node)

                for nei, weight in graph[node]:
                    if(nei not in visited):
                        queue.append((nei, val * weight))
            
            return -1.0
        
        # store the results from the queries and return it
        q_results = []
        for a,b in queries:
            q_results.append(bfs(a,b))
        
        return q_results



sol = Solution()
r = sol.calcEquation([["a","b"],["b","c"]],   [2.0,3.0],    [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
print(r)