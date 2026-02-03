#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 14:47:23 2025

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
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy 
        for _ in range(m-1):
            pre = pre.next 

        curr = pre.next 
        then = curr.next 
        
        for _ in range(n-m):
            curr.next = then.next 
            then.next = pre.next 
            pre.next = then 
            then = curr.next 
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