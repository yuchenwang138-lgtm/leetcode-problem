#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 00:27:35 2025

@author: macbook
"""

list = [1,7,3,5,9,4,8]
n = len(list)
dp = [0] * n
for i in range(n):
    dp[i] = 1
    for j in range(i):
        if list[j] < list[i]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))