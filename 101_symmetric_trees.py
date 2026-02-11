# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import defaultdict, deque


class Solution:
    # potential solutions: bfs palindrome, recursive, invert + eq
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # check if tree is mirrored
        # recursive: check if left.left = right.right
        #                  and left.right = right.left
        # and for every child node, same thing
        tree1 = root.left
        tree2 = root.right
        self.symmetry = True
        def check_crossed(tree_left, tree_right):
            if (tree_left is None and tree_right is None): 
                return

            # because they're not both none, if either is none it can't be eq
            elif (tree_left is None or tree_right is None):
                self.symmetry = False
                return

            elif (tree_left.val != tree_right.val):
                self.symmetry = False
                return 
            
            else:
                check_crossed(tree_left.left, tree_right.right)
                check_crossed(tree_left.right, tree_right.left)

        check_crossed(tree1, tree2)
        return self.symmetry


#tests
sol = Solution()
#[1,2,2,3,4,4,3]
lst = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
res=sol.isSymmetric(lst)
                
print(res)
                


