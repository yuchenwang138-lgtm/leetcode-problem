#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 19:28:37 2025

@author: macbook
"""

n = int(input("请输入有多少个房子:"))

row = list(map(int,input("请输入每个房子有多少个金币，用空格分割:").split()))


def solve(row):
    if n == 0:
        return 0
    if n == 1:
        return row[0]
    dp = [0] * n
    dp[0] = row[0]
    dp[1] = max(row[0],row[1])
    for i in range(2,n):
        dp[i]=max(dp[i-1],dp[i-2]+row[i])
    return dp[n-1]

print(solve(row))