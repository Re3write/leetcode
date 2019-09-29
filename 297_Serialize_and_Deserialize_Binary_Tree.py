#自己写的，正确，但超时

class Codec:

    def depth(self, root):
        if root == None:
            return 0
        left = self.depth(root.left) + 1
        right = self.depth(root.right) + 1
        return max(left, right)

    def serialize(self, root):
        self.length = self.depth(root)
        queue = []
        result = []
        node = root
        queue.append((root, 1))
        while queue:
            node, dep = queue.pop(0)
            if dep <= self.length:
                queue.append((node.left, dep + 1) if node != None else (None, dep + 1))
                queue.append((node.right, dep + 1) if node != None else (None, dep + 1))
                result.append(node.val if node != None else None)
                # print(result)
        return result

        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        queue = []
        if data[0] == None:
            return None
        root = TreeNode(data[0])
        node = root
        flag = 0
        for value in data[1:]:
            if flag == 0 and value != None:
                node.left = TreeNode(value)
                queue.append(node.left)
                flag = 1
            elif flag == 0 and value == None:
                queue.append(None)
                flag = 1
            elif flag == 1 and value != None:
                node.right = TreeNode(value)
                queue.append(node.right)
                node = queue.pop(0)
                flag = 0
            elif flag == 1 and value == None:
                queue.append(None)
                node = queue.pop(0)
                flag = 0
        return root