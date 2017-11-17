
import random #appeller la fonction


def create_grid(grid):
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)

#MAIN

grid=[]

x=4
y=4

create_grid(grid)

grid[x][y]="8"

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


rand = random.randint(1,10)

print rand
