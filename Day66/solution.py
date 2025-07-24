from collections import defaultdict
from math import inf

class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        # Perform DFS to calculate xor of the subtree rooted at node `i`
        # excluding any visited node `fa` and the edge broken at node `x`
        def dfs(node, parent, exclude_node):
            result = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent and neighbor != exclude_node:
                    result ^= dfs(neighbor, node, exclude_node)
            return result

        # Another DFS to calculate the minimum score after breaking the edge
        # at node `x` by considering different divisions of the tree and
        # updating the answer with the possible score
        def dfs_with_score(node, parent, exclude_node):
            nonlocal total, subtree_xor, min_score
            result = nums[node]
            for neighbor in graph[node]:
                if neighbor != parent and neighbor != exclude_node:
                    subtree_result = dfs_with_score(neighbor, node, exclude_node)
                    result ^= subtree_result
                    remaining_xor = subtree_xor ^ subtree_result
                    rest_of_tree_xor = total ^ subtree_xor
                    max_xor = max(subtree_result, remaining_xor, rest_of_tree_xor)
                    min_xor = min(subtree_result, remaining_xor, rest_of_tree_xor)
                    score_difference = max_xor - min_xor
                    min_score = min(min_score, score_difference)
            return result

        # Create a graph from the edges
        graph = defaultdict(list)
        for start_node, end_node in edges:
            graph[start_node].append(end_node)
            graph[end_node].append(start_node)

        # Calculate the total xor of all values
        total = 0
        for value in nums:
            total ^= value

        # Initialize minimum score to infinity
        min_score = inf

        # Iterate over all nodes in the graph
        for i in range(len(nums)):
            # Iterate over its connected edges to break one at a time
            for j in graph[i]:
                # Perform dfs to get xor of subtree after breaking edge between i and j
                subtree_xor = dfs(i, -1, j)
                # Perform dfs to get the minimum score after breaking edge between i and j
                dfs_with_score(i, -1, j)
              
        # Return the minimum score found
        return min_score