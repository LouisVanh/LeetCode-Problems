# from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
#     def __str__(self):
#         return str(self.val)

# class Solution:
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         node_we_are_looking_for = None
#         max_depth_found = 0

#         def dfs(node):
#             nonlocal node_we_are_looking_for, max_depth_found
#             if node is None:
#                 return 0

#             left = dfs(node.left)
#             right = dfs(node.right)
#             curr_height = max(left, right) + 1

#             if left == right:
#                 if curr_height >= max_depth_found:
#                     max_depth_found = curr_height
#                     node_we_are_looking_for = node
#                     # Uncomment to debug:
#                     # print(f"Updated LCA: {node.val} at height {curr_height}")

#             return curr_height

#         dfs(root)
#         return node_we_are_looking_for


# sol = Solution()
# # r = sol.lcaDeepestLeaves(TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(None), TreeNode(6, TreeNode(None)))), TreeNode(4, TreeNode(None), TreeNode(5))))
# r = sol.lcaDeepestLeaves(TreeNode(1, TreeNode(2, TreeNode(4))))
# print(r)

i couldnt do it.