# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        queue = deque([0])
        visited = set([0])

        for i in range(len(rooms)):
            graph[i].extend(rooms[i])
  
        while queue:
            key = queue.popleft()

            for negh in graph[key]:
                if negh not in visited:
                    visited.add(negh)
                    queue.append(negh)
        return len(visited) == len(rooms)
            

             


            
 

        