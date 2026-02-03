#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 17:51:44 2025

@author: macbook
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self , head , m , n ):
        # write code here
        if not head or m==n:
            return head
        #定义了一个哑巴节点dummy，为了计数方便
        dummy = ListNode(0)
        dummy.next = head 
        a = dummy 
        for _ in range(m-1):
            a = a.next 
        b = a.next
        x_p,x = a,b 
        # a与b代表开始反转的前一个节点与开始反转的节点，
        
        # 这里x_n用于记录正在反转的x的下一个节点，让x指向xp后，xp与x能向后移动
        for _ in range(n-m+1):
            x_n = x.next
            x.next = x_p 
            x_p,x = x,x_n 
        #a最终要指向反转的最后一个节点，也就是x_p的最终值
        # b最终要指向反转的最后一个节点的下一个节点，也就是x的最终值
        a.next = x_p 
        b.next = x
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
new_head = solution.reverseBetween(head, 2, 4)
curr = new_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next