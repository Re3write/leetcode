class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            nodeval = preorder.pop(0)
            index = inorder.index(nodeval)
            node = TreeNode(nodeval)
            node.left=self.buildTree(preorder,inorder[:index])
            node.right = self.buildTree(preorder,inorder[index+1:])
            return node
        return None