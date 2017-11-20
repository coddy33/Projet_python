#-*- coding: utf-8 -*-

import random

def create_grid(grid):
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)

def print_grid(grid):
    print "\n\n\n"
    print "------------ VIRUS KILLER ---------------"
    print "-----------------------------------------"
    y=0
    while y<=9:
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

def energy(grid):
    for i in range(8):
        r=0    
        x=random.randint(0,9)
        listtmp=grid[x]
        while r==0:
            y=random.randint(0,9)
            if listtmp[y]!="W" and listtmp[y] !=0 and listtmp[y]!="A" and listtmp[y]!="V":
                grid[x][y]="A"
                break
            if listtmp[y]=="W" or listtmp[y]==0 or listtmp[y]=="A" or listtmp[y]=="V":
                continue

def spawn_virus(grid):
    for i in range(4):
        r=0
        x=random.randint(0,9)
        listtmp=grid[x]
        while r==0:
            y=random.randint(0,9)
            if listtmp[y]!="W" and listtmp[y]!=0 and listtmp[y]!="A" and listtmp[y]!="V":
                grid[x][y]="V"
                break
            if listtmp[y]=="W" or listtmp[y]==0 or listtmp[y]=="A" or listtmp[y]!="V":
                continue

def repop_energy():
    totA=0
    for i in range(10):
        for h in range(10):
            if grid[i][h]=="A":
                totA=totA+1
    if totA<8:
        pop(nb=8-totA,mol="A")

def pop(nb,mol): #on defini le nombre de pop=nb ; puis quelle molecule doit pop=mol
    for i in range(nb):
        r=0    
        x=random.randint(0,9)
        listtmp=grid[x]
        while r==0:
            y=random.randint(0,9)
            if listtmp[y]!="W" and listtmp[y] !=0 and listtmp[y]!="A" and listtmp[y]!="V":
                grid[x][y]=mol
                break
            if listtmp[y]=="W" or listtmp[y]==0 or listtmp[y]=="A" or listtmp[y]=="V":
                continue

#MAIN

grid=[]

x=4
y=3

create_grid(grid)

grid[x][y]=0

hardcore(grid)
pop(nb=8,mol="A")#pop ATP
pop(nb=4,mol="V")#pop Virus
repop_energy()
print_grid(grid)


