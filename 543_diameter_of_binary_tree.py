# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_path = 0  # This stores the max diameter

        def traverse(root: Optional[TreeNode]) -> int:
            nonlocal longest_path
            if root is None:
                return 0  # Base case: height of an empty tree is 0

            longest_left = traverse(root.left)  # Height of left subtree
            longest_right = traverse(root.right)  # Height of right subtree
            
            # Update the longest path (Diameter = longest_left + longest_right)
            longest_path = max(longest_path, longest_left + longest_right)

            return 1 + max(longest_left, longest_right)  # Height of current node

        traverse(root)
        return longest_path  # Return diameter (edges, not nodes)

# Example Tree
root = TreeNode(5)
root.left = TreeNode(8)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)

sol = Solution()
r = sol.diameterOfBinaryTree(root)
print(r)  # Output should be the longest path between two leaves
