def isSymmetric(root: TreeNode) -> bool:
    def help(left, right):
        # left/right都为空节点
        if not left and not right:
            return True
        # left/right有一个为空
        if not (left and right):
            return False
        # 值是否相等
        if left.val != right.val:
            return False
        # 将左右字节对称递归比较
        return help(left.left, right.right) and help(left.right, right.left)

    return help(root.left, root.right) if root else True

