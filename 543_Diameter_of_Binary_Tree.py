class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_length = 0
        def preorder(root):
            if root == None:
                return 0
            left = preorder(root.left)
            right = preorder(root.right)
            self.max_length = max(self.max_length,left+right)
            return max(left,right)+1
        preorder(root)
        return self.max_length