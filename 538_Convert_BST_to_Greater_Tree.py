##自己写的深拷贝递归遍历，正确，但时间超时
class Solution:
    import copy
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.root = root  # 原来树的入口
        self.newroot = copy.deepcopy(root)  # 新的树的入口

        def add(root, val):
            if root == None:
                return 0
            if root.val < val:
                value = add(root.right, val)
            else:
                value1 = add(root.left, val) + root.val
                value2 = add(root.right, val) + root.val
                value = value1 + value2 - root.val

            return value

        def sum(root):
            if root == None:
                return
            root.val = add(self.newroot, root.val)
            sum(root.left)
            sum(root.right)

        sum(root)
        return root



#逆中序遍历
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.num = 0
        def depthfirstsearch(root):
            if root is None:
                return
            else:
                depthfirstsearch(root.right)
                self.num = self.num + root.val
                root.val = self.num
                depthfirstsearch(root.left)
                return root
        return depthfirstsearch(root)


