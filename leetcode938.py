class Solution:
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans = self.ans + node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
