#-*- coding: utf-8 -*-

def create_grid(grid):
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)


def print_grid(grid):
    print "\n\n\n"
    print "------------ VIRUS KILLER ---------------"
    print "-----------------------------------------"
    y=0
    while y<9:
        x=0
        for h in range(9):
            print "|",grid[x][y], 
            x=x+1
        print "|",grid[x][y],"|"
        print"-----------------------------------------"
        y=y+1
    

def easy(grid):
    listx=[2,7,4,0,4,1,6,3,8,2]
    listy=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]="W"

def normal(grid):
    listx=[2,8,7,3,7,4,0,2,0,4,9,1,6,1,6,3,0,8,2,6]
    listy=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]="W"

def hardcore(grid):
    listx=[2,8,3,6,7,1,4,7,0,2,9,0,4,5,7,1,3,9,1,6,7,3,4,5,6,0,8,9,2,6]
    listy=[0,0,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]="W"

#MAIN

grid=[]

x=4
y=3

create_grid(grid)

grid[x][y]=0

#TEST GRID
#for i in range(10):
    #print grid[i]
hardcore(grid)
print_grid(grid)


