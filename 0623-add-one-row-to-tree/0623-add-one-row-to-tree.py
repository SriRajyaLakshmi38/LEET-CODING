# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
      # Edge Case: if we need to insert at top parent node then connect to root Just like u would in linked list
        if depth == 1: # since in a tree depth starts at 1
            node = TreeNode(val, left = root)
            return node
        
        def dfs(root, curDepth):
            if not root:
                return
            if curDepth == depth-1:
                # add the new nodes on the left and right 
                root.left = TreeNode(val, left = root.left)
                root.right = TreeNode(val, right = root.right)

            dfs(root.left, curDepth + 1)
            dfs(root.right, curDepth + 1)
            
            
        dfs(root, 1)
        return root