#-*- coding: utf-8 -*-

def create_grid(grid):
    for i in range(10):
        list=[1,2,3,4,5,6,7,8,9,10]
        grid.append(list)

#MAIN

grid=[]

x=5
y=4

create_grid(grid)

grid[x][y]=0

for i in range(10):
    print grid[i]




