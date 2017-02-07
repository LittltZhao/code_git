# -*- coding:utf-8 -*-

def islandPerimeter(grid):
    count
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                continue
            elif grid[i][j]==1:
                count+=4
                if i>0 and grid[i-1][j]==1:#从上到下
                    count-=2
                if j>0 and grid[i][j-1]==1:#从左到右
                    count-=2
    return count
