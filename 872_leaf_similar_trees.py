from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node, list_to_track):
            if(node == None):
                return 0, list_to_track
            
            # post order traversal
            left, _ = dfs(node.left, list_to_track)
            right, _ = dfs(node.right, list_to_track)

            # add to the list in the post order traversal order, if it's a leaf
            if(left == 0 and right == 0):
                list_to_track.append(node.val)

            return (max(left, right) + 1, list_to_track)
        

        return dfs(root1, [])[1] == dfs(root2, [])[1]
    
sol = Solution()
r = sol.leafSimilar(TreeNode(2, TreeNode(5), TreeNode(6)), TreeNode(9999, TreeNode(5), TreeNode(6)))
print(r)
r = sol.leafSimilar(TreeNode(2, TreeNode(5), TreeNode(6)), TreeNode(2, TreeNode(4), TreeNode(6)))
print(r)
        
