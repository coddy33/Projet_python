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

#TEST GRID
#for i in range(10):
    #print grid[i]

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


