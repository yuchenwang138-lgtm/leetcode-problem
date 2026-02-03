#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 18:59:38 2025

@author: macbook
"""
# 输入行数
n = int(input("请输入行数: "))

# 创建二维矩阵
matrix = []

for i in range(n):
    # 输入每行数字，用空格分隔，并转为整数列表
    row = list(map(int, input(f"请输入第{i+1}行数字，用空格分隔: ").split()))
    matrix.append(row)
def solve(matrix):
    dp = [[0]* (i+1) for i in range(n)]
    # path 记录下当前的最大值是由上一层的j-1还是j得到
    path = [[-1]*(i+1) for i in range(n)]
    dp[0][0]=matrix[0][0]
    for i in range(1,n):
        for j in range(i+1):
            if j==0:
                dp[i][j]=matrix[i][j]+dp[i-1][j]
                path[i][j]=j
            elif j==i:
                dp[i][j]=matrix[i][j]+dp[i-1][j-1]
                path[i][j]=j-1
            else:
                if dp[i-1][j-1]>dp[i-1][j]:
                    dp[i][j]=matrix[i][j]+dp[i-1][j-1]
                    path[i][j]=j-1
                else:
                    dp[i][j]=matrix[i][j]+dp[i-1][j]
                    path[i][j]=j
    #得到最后一层的j指标
    j = dp[n-1].index(max(dp[n-1]))
    max_path = []
    for i in range(n-1,-1,-1):
        max_path.append(matrix[i][j])
        j = path[i][j]
    max_path.reverse()
    return dp,max_path
dp,max_path = solve(matrix)
print(max(dp[n-1]))
print(max_path)


