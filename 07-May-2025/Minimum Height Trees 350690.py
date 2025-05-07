# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

 

class Solution:
    def findMinHeightTrees(self, number_of_nodes: int, connections: List[List[int]]) -> List[int]:
        if number_of_nodes == 1:
            return [0]

        graph = defaultdict(set)
        for node_a, node_b in connections:
            graph[node_a].add(node_b)
            graph[node_b].add(node_a)

        leaf_nodes = deque()
        for node in range(number_of_nodes):
            if len(graph[node]) == 1:
                leaf_nodes.append(node)

        remaining_nodes = number_of_nodes
        while remaining_nodes > 2:
            number_of_leaves = len(leaf_nodes)
            remaining_nodes -= number_of_leaves

            for _ in range(number_of_leaves):
                leaf = leaf_nodes.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    leaf_nodes.append(neighbor)

        return list(leaf_nodes)
