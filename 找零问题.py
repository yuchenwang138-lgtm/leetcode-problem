#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 23:16:14 2025

@author: macbook
"""
#要凑出的面值为m 
n = int(input("请输入有多少种硬币:"))

rows = list(map(int,input("请输入每个硬币的面值，用空格分割:").split()))

def solve(m):
    dp = [float('inf')] * (m+1)
    dp[0] = 0
    for i in range(1,m+1):
        for row in rows:
            if i-row >= 0 and dp[i-row] != float('inf'):
                dp[i] = min(dp[i-row]+1,dp[i])
    return dp[m]
print(solve(31))
print(solve(58))
print(solve(3))
                
