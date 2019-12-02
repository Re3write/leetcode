class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        result = []
        nextlevel = []
        nn = []
        queue.append(root)
        while queue:
            temp = queue.pop(0)
            nn.append(temp.val)
            if temp.left:
                nextlevel.append(temp.left)
            if temp.right:
                nextlevel.append(temp.right)
            if not queue:
                queue = nextlevel
                result.append(nn)
                nextlevel = []
                nn = []
        return result