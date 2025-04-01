from typing import List
from collections import defaultdict, deque
class Solution:
    # Couldn't get this to work :( 650/680 test cases passed
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        # Make adjacency list
        #make function intersect(a,b):
        def intersect(a,b): # takes in 2 arrays
            amount_of_distinct_integers = []
            for i in range(len(a)):
                for j in range(len(b)):
                    if(a[i] == b[j] and a[i] not in amount_of_distinct_integers):
                        amount_of_distinct_integers.append(a[i])

            
            return len(amount_of_distinct_integers)
        
        adjacency_list = defaultdict(list)
        for i in range(len(properties)):
            adjacency_list[i]

        i, j = 0, 1
        # print(len(properties))
        while i != len(properties):
            # print(i)
            j = i+1
            while j != len(properties):
                # print(f"{i} and {j} are tested")
                if(intersect(properties[i], properties[j]) >= k):
                    # print(f"{i} and {j} are intersecting")
                    adjacency_list[i].append(j)
                    adjacency_list[j].append(i)
                j+=1
            i+=1
        #print(adjacency_list)
        
        counter = 0
        visited = set()
        while adjacency_list:
             val, list_of_connected_nodes = adjacency_list.popitem()
             if(len(list_of_connected_nodes) == 0): 
                counter+=1
                
             else: # There's nodes connected to this, pop them from the adjancency_list
                for node in list_of_connected_nodes:
                    if(node not in visited):
                        visited.add(node)
                        adjacency_list.pop(node)
                        counter+=1
                        break

        return counter
sol = Solution()
# r = sol.numberOfComponents([[1,2],[1,1]], 1)
# print(r)
r = sol.numberOfComponents([[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], 1)
print(r)