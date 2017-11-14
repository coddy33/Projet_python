#-*- coding: utf-8 -*-

def interface():
    
    for i in range(21):
        if i % 2 ==0:
            print ligne
        else:
            print colonne 


def create_grid(grid):
    ligne = "+----+----+----+----+----+----+----+----+----+----+"
    colonne = "|    |    |    |    |    |    |    |    |    |    |"
    list=[1,2,3,4,5,6,7,8,9,10]
    for i in range(21):
        if i % 2 ==0:
            print ligne
            
        else:
            print "| ",grid.append(list)
       

#MAIN

grid=[]

x=5
y=4

create_grid(grid)

grid[x][y]=0

for i in range(10):
    print grid[i]


