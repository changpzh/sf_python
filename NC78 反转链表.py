# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param head ListNode类 
# @return ListNode类
#                         head
#                         node1    ->  node2    ->   node3     -> None
# 这是一个单向链表：node = [val|next] -> [val|next] -> [val|next] -> None
class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        new_list_node = None
        cur = head  # 把链表的头赋值给cur
        while cur:
            temp = cur.next
            cur.next = new_list_node    # 把新列表接到当前列表后面
            new_list_node = cur         # 把组装好的当前列表赋值给新列表
            cur = temp                  # 移动 cur 位置
        return new_list_node
'''
以 {1， 2， 3}的链表为例：[val=1 | next=node2] -> [val=2 | next=node3] -> [val=3 | next=None]
1. head第一次指向 node1 =[val=1| next=node2]，所以cur也指向node1
2. while cur：
    第1次循环：cur = [val=1 | next=node2]
        temp = cur.next         # 此时 temp 就是 [val=2 | next=node3] 
        cur.next = new_listNode # cur的next就从node2变为None了，此时cur 为 [val=1 | next=None]
        new_listNode = cur      # 新的链表从None变为[val=1 | next=None]
        cur = temp              # cur 位置跳转到 [val=2 | next=node3]
    
    第2次循环：cur = [val=2 | next=node3]
        temp = cur.next         # 此时 temp 就是 [val=3 | next=None] 
        cur.next = new_listNode # cur的next就从node3变为node1了,此时 cur 为 [val=2 | next=node1]-> [val=1 | next=None]
        new_listNode = cur      # 新的链表 为 [val=2 | next=node1]-> [val=1 | next=None]
        cur = temp              # cur 位置跳转到 [val=3 | next=None]
        
    第3次循环：cur = [val=3 | next=None]
        temp = cur.next         # 此时 temp 就是 None 
        cur.next = new_listNode # 此时 cur 为 [val=3 | next=node2]->[val=2 | next=node1]-> [val=1 | next=None]
        new_listNode = cur      # 此时 新的链表为 [val=3 | next=node2]->[val=2 | next=node1]-> [val=1 | next=None]
        cur = temp              # cur 位置跳转到 None

    第4次循环：cur = None, 退出while循环
'''

"""
算法思路：
  定义新链表为None
  while 当前节点不为None：
      临时变量存储当前节点之后的链表
      将当前节点的next指向新的链表，第一次指向None
      更新新的链表（将当前节点拷贝给新的链表 ）
      移动当前节点位置到下一个链表（临时变量）
  返回逆序之后的新链表
"""
