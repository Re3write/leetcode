class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root,minval,maxval):
            if not root:
                return True
            if root.val > minval and root.val < maxval:
                return helper(root.left,minval,root.val) and helper(root.right,root.val,maxval)
            return False
        return helper(root,float('-inf'),float('inf'))