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






#MAIN

grid=[]

x=5
y=4

create_grid(grid)

grid[x][y]=0

#TEST GRID
#for i in range(10):
    #print grid[i]
easy(grid)
print_grid(grid)


