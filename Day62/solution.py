from collections import defaultdict

# A TrieNode represents a folder with children and a 'deleted' flag
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)  # Maps folder names to child TrieNodes
        self.deleted = False  # Flag to mark if this node is part of a duplicate subtree

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        ans = []          # Stores the final remaining paths
        path = []         # Temporarily holds current path during DFS
        subtree_to_nodes = defaultdict(list)  # Maps serialized subtrees to list of nodes

        # Sort paths to build the Trie in consistent order
        paths.sort()

        root = TrieNode()

        # Build the Trie structure from given paths
        for p in paths:
            node = root
            for s in p:
                node = node.children[s]

        """
        Traverse the Trie and serialize each subtree.
        Each subtree string is stored in `subtree_to_nodes` dict.
        If two nodes produce the same serialized string, they are duplicates.
        """
        self.build_subtree_to_nodes(root, subtree_to_nodes)

        # Mark all nodes that are part of duplicate subtrees
        for nodes in subtree_to_nodes.values():
            if len(nodes) > 1:  # Only consider duplicates
                for node in nodes:
                    node.deleted = True

        """
        Perform DFS to construct final folder paths.
        Skip nodes that are marked deleted.
        """
        self.construct_path(root, path, ans)

        return ans

    # Recursively serialize subtrees using post-order traversal
    def build_subtree_to_nodes(self, node: TrieNode, subtree_to_nodes: dict) -> str:
        subtree = "("  # Begin serialization
        for s, child in node.children.items():
            subtree += s + self.build_subtree_to_nodes(child, subtree_to_nodes)
        subtree += ")"  # End serialization

        # Don't store empty folders
        if subtree != "()":
            subtree_to_nodes[subtree].append(node)

        return subtree

    # DFS to collect remaining folder paths (not marked deleted)
    def construct_path(self, node: TrieNode, path: List[str], ans: List[List[str]]):
        for s, child in node.children.items():
            if not child.deleted:  # Skip deleted folders
                path.append(s)  # Add current folder to path
                self.construct_path(child, path, ans)  # Recurse
                path.pop()  # Backtrack

        # Add current path to result if it's not empty
        if path:
            ans.append(path[:])
