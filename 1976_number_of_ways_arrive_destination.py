from typing import List
from collections import defaultdict
import heapq
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1; make graph
        graph = defaultdict(list)
        for u, v, time in roads:
            # print(f"u: {u}, v:{v}, time: {time}")
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Step 2: initialise dist array and ways array
        dist = [(float('inf'))] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        # print(dist)

        # Step 3: init heap (time to node)
        heap = [(0,0)] # it takes 0 time to get to node 0 (we start there)

        # Step 4: mod
        MOD = 10**9 + 7 # modulo needed for large numbers (given in question, not standard)

        # Step 5: loop through heap to find shortest time (distance)
        while heap:
            curr_time, u = heapq.heappop(heap)
            # If it takes longer than previous paths to get to the same node, no point - this will never be shortest
            if(curr_time > dist[u]):
                continue

            for v, time in graph[u]:
                # set the new time to however long it took to get to the current node + the time to the adjacent node
                new_time = curr_time + time

                if(new_time > dist[v]):
                    continue
                elif(new_time == dist[v]):
                    # if 5 trains got me to 'u', the ways to 'v' is however many we already had + 5
                    ways[v] = (ways[v] + ways[u]) % MOD
                elif(new_time < dist[v]):
                    # if 5 trains got me to 'u', the ways to v is the new shortest, so 5 paths take me here
                    ways[v] = ways[u]
                    dist[v] = new_time 
                    heapq.heappush(heap, (new_time,v))
            
        return ways[n-1]



sol = Solution()
r=sol.countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]])
print(r)
