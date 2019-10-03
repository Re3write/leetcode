# 由于每个节点只有唯一一个父节点，我们可以使用到字典的value-key的形式（节点-父节点）
# 字典中预置根节点的父节点为None。
#
# 字典建立完成后，二叉树就可以看成一个所有节点都将最终指向根节点的链表了。
#
# 于是在二叉树中寻找两个节点的最小公共节点就相当于，在一个链表中寻找他们相遇的节点

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {root:None}
        def dfs(node):
            if node:
                if node.left:
                    dic[node.left] = node
                if node.right:
                    dic[node.right] = node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        l1, l2 = p, q
        while(l1!=l2):              #精髓  @maomaochong 你可以这样考虑，小明和小刚约好一起到同一个车站去打车上学，后面的路程大家是相同的，但是从家到车站的距离是不同的，
                                    # 想办法让他们两个走过相同的距离就可以找到碰面的地点，如果小明到车站的路程是3，小刚的路程是4，车站到学校的距离是5，明显小明先到车站，
                                    # 让小明先走到学校这个时候他走了8，而此时小刚走的距离也是8，但小刚离学校还有1的距离，这个时候让小明瞬移到小刚家再往车站走距离1后，小刚到达学校，
                                    # 让小刚瞬移到小明家往车站走，这个时候大家离车站距离都是3，放心大胆往前走一定能碰面
            l1 = dic.get(l1, q)
            l2 = dic.get(l2, p)
        return l1


# 第二种思路
# 一旦我们找到了 p 和 q，我们就可以使用父亲字典获得 p 的所有祖先，并添加到一个称为祖先的集合中。
# 同样，我们遍历节点 q 的祖先。如果祖先存在于为 p 设置的祖先中，这意味着这是 p 和 q 之间的第一个共同祖先（同时向上遍历），
# 因此这是 LCA 节点。
#


#第三种思路
# 从根节点开始遍历树。
# 如果当前节点本身是 p 或 q 中的一个，我们会将变量 mid 标记为 true，并继续搜索左右分支中的另一个节点。
# 如果左分支或右分支中的任何一个返回 true，则表示在下面找到了两个节点中的一个。
# 如果在遍历的任何点上，左、右或中三个标志中的任意两个变为 true，这意味着我们找到了节点 p 和 q 的最近公共祖先。
#公共祖先找到后再向上只有1条边为true 所以不担心被覆盖

class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans





#我的极low双递归解法
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = []
        pp = p.val
        qq = q.val

        def find(root, flag):
            if root == None:
                return flag
            if root.val == pp or root.val == qq:
                flag = flag + 1
            flag = find(root.left, flag)
            flag = find(root.right, flag)
            return flag

        def compare(root):
            if root == None:
                return
            if find(root, 0) == 2:
                result.append(root.val)
            print(result)
            compare(root.left)
            compare(root.right)

        compare(root)
        return result[-1]


