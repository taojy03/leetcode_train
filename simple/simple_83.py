"""
83.删除排序链表中的重复元素
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
输入：head = [1,1,2]
输出：[1,2]
输入：head = [1,1,2,3,3]
输出：[1,2,3]

提示：
链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列
"""
from typing import List, Optional

class ListNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.next = None


def delete_duplicates(head):
    if not head:
        return head
    p = head
    while p.next:
        if p.next.val == p.val:
            p.next = p.next.next
        else:
            p = p.next
    return head


if __name__ == '__main__':
    head = ListNode(1)
    Node1 = ListNode(1)
    Node2 = ListNode(2)
    head.next = Node1
    Node1.next = Node2

    res = deleteDuplicates(head)
    
    while res != None:
        print(res.val)
        res = res.next

#考虑极端情况，前中后