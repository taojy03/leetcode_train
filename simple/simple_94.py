"""
94.二叉树的中序遍历
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
输入：root = [1,null,2,3]
输出：[1,3,2]

提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        def inorder(Node):
            if Node == None:
                return
            inorder(Node.left)
            result.append(Node.val)
            inorder(Node.right)
        inorder(root)
        return result