class Solution:
    def __init__(self):
        self.total = 0

    def sumsingle(self, root, sum):
        if root == None:
            return
        sum = sum - root.val
        if sum == 0:
            self.total += 1
        self.sumsingle(root.left, sum)
        self.sumsingle(root.right, sum)
        return

    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        self.sumsingle(root, sum)
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        return self.total