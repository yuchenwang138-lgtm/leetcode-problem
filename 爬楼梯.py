#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 18:55:07 2025

@author: macbook
"""
def solve(n):
    if n==1 or n==0:
        return 1
    dp = [0] * (n+1)
    dp[0] = dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(solve(5))