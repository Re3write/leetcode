class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(root):
            if not root:
                return 0
            return max(helper(root.left),helper(root.right))+1
        return helper(root)