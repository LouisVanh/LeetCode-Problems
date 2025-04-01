from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        # Base case: If root is None, return an empty list
        if root is None:
            return result
        
        # Recursively traverse left subtree
        result.extend(self.inorderTraversal(root.left))
        
        # Visit the root (parent) node
        result.append(root.val)
        
        # Recursively traverse right subtree
        result.extend(self.inorderTraversal(root.right))
        
        return result

sol = Solution()
r = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(sol.inorderTraversal(r))  # Expected Output: [1, 3, 2]

# explanation: path of execution (balanced A BC DEFG tree)
# - get root node (A)
# - visit left (B)
# - visit left (D)
# - try to visit left root given is none, give nothing
# - append itself D
# - try to visit right, none, nothing
# - parent B
# - right E
# - root node has exhausted left branch (the first extend is done)
# ...