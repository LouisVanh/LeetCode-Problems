from typing import List
from collections import deque, defaultdict
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        total_complete = 0
        visited = set()
        adjacency_list = defaultdict(list)
        for el1, el2 in edges:
            adjacency_list[el1].append(el2)
            adjacency_list[el2].append(el1)
        
        # Ensure isolated nodes are included
        for i in range(n):
            adjacency_list[i]

        # Do a breadth first search on each element, confirm that it has the same amount of neighbours
        def bfs(start):
            nonlocal total_complete
            if(start in visited):
                return
            
            queue = deque([(start)])
            component = []

            while queue:
                current = queue.popleft()
                if(current in visited):
                    continue # go to next element, already checked this one
                visited.add(current)
                
                # add it to the component
                component.append(current)

                for neigh in adjacency_list[current]:
                    if neigh not in visited:
                        queue.append(neigh)


            # After while loop is done: (component is formed)
            component_size = len(component) # preprocess it
            is_complete = True
            for node in component:
                # Every node should have n-1 other nodes
                if(len(adjacency_list[node]) != component_size-1):
                    is_complete = False
                    break
            
            if(is_complete): 
                print(component)
                total_complete+=1

        for i in range(n):
            bfs(i)
        return total_complete
        
sol = Solution()
r = sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]])
print(r)
r = sol.countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]])
print(r)
