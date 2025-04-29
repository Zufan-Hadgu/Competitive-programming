# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: 
    graph = defaultdict(list)
    for path in times:
        u, v, w = path   
        graph[u].append((v,w))   
    minheap = [(0,k)]
    visited = set()
    output = 0

    while minheap:
        weight,node  = heapq.heappop(minheap)
        
        if node in visited:
            continue
        visited.add(node)
        output = max(output,weight)

        for new_node,time in graph[node]:
            if new_node not in visited:
                heapq.heappush(minheap, (time + weight, new_node))  

    return output if(len(visited) == n) else -1



     