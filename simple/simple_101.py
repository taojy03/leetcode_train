"""
101.对称的二叉树
给你一个二叉树的根节点 root ， 检查它是否轴对称。
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false
 提示：
树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100
 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""
"""
和相同的树一样，在根节点的位置是对称轴不用管，相同的树是左左一样、右右一样，而对称的树是左右一样、右左一样
"""
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if (not p and not q):
        return True
    if (not p or not q):
        return False
    if (p.val != q.val):
        return False
    left = isSameTree(p.left, q.right)
    right = isSameTree(p.right, q.left)
    return left and right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    return isSameTree(root.left, root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3) 
    root.right.right = TreeNode(3)
    print(isSymmetric(root))