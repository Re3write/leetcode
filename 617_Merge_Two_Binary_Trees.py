# // 617.
# java  合并二叉树
# / **
# *Definition
# for a binary tree node.
# *public
#
#
# class TreeNode {
# * int val;
# * TreeNode left;
# * TreeNode right;
# * TreeNode(int x) {val = x;}
# *}
#
# * /
# // 方法1生成新树
#
#
# class Solution {
# public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
# if (t1 == null & & t2 == null){
#
#
# return null;
# }
# TreeNode
# t3 = new
# TreeNode((t1 == null?0:t1.val) + (t2 == null?0:t2.val));
# t3.left = mergeTrees(t1 == null?null: t1.left, t2 == null?null: t2.left);
# t3.right = mergeTrees(t1 == null?null: t1.right, t2 == null?null: t2.right);
# return t3;
# }
# }
# // 方法2把2并到1上
#
#
# class Solution {
# public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
# if ((t1 == null & & t2 == null) | | t1 == null){
#
#
# return t;
# }
#
# if (t2 == null){
# return t1;
# }
# t1.val += t2.val;
# t1.left = mergeTrees(t1.left, t2.left);
# t1.right = mergeTrees(t1, right, t2.right);
# return t1;
# }
# }


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and t2:
            return t2
        elif t1 and t2:
            t1.val = t2.val+t1.val
            t1.left = self.mergeTrees(t1.left,t2.left)
            t1.right = self.mergeTrees(t1.right,t2.right)
        return t1
