class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        self.ans = 0
        def dfs(root):
            if not root: return []
            if not root.left and not root.right: return [1]
            left = dfs(root.left)
            right = dfs(root.right)
            for i in left:
                for j in right:
                    if i+j <= distance:
                        self.ans += 1
            return [i+1 for i in left+right if i+1 < distance]
        dfs(root)
        return self.ans