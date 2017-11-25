#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur

import sys
import os
import random


#Create Grid

def create_grid(grid):
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)

def print_grid(grid):
    print "\n"
    print "----------- ","\x1b[33;1mVIRUS KILLER","\x1b[37;0m --------------"
    print "\x1b[30;1m-----------------------------------------\x1b[37;1m"
    y=0
    while y<=9:
        x=0
        for h in range(9):
            print "\x1b[30;1m|\x1b[37;1m",grid[x][y], 
            x=x+1
        print "\x1b[30;1m|\x1b[37;1m",grid[x][y],"\x1b[30;1m|\x1b[37;1m"
        print"\x1b[30;1m-----------------------------------------\x1b[37;1m"
        y=y+1


def pop(nb,mol,loc): #on defini le nombre de pop=nb ; puis quelle molecule doit pop=mol
    for i in range(nb):
        r=0    
        x=random.randint(0,9)
        listtmp=grid[x]
        loc_virus=[]
        while r==0:
            y=random.randint(0,9)
            if listtmp[y]!=wall and listtmp[y] !=0 and listtmp[y]!=ATP and listtmp[y]!=virus:
                grid[x][y]=mol
                if mol == virus:
                    loc_virus.append(x)
                    loc_virus.append(y)
                    loc.append(loc_virus)
                break
            if listtmp[y]==wall or listtmp[y]==0 or listtmp[y]==ATP or listtmp[y]==virus:
                continue
        
        
#Movment Player

def move_player(G,P,I,P_V):
    movement = raw_input("où voulez-vous aller ?")
    nbr_case=input("de combien de cases voulez-vous vous déplacer ?") # erreur possible si input string
    x=P[0]
    y=P[1]
    x,y = move(G,P,I,movement,nbr_case,x,y,P_V)
    os.system("clear")
    G[x][y]= perso
    P[0]=x
    P[1]=y

def move_virus(G,P,I,P_V):
    for i in range(len(P_V)):
        nbr_case=random.randint(1,9) #nb de cases entre 1 et 9
        listdirect=["z","q","s","d"]
        pos=random.randint(0,3)
        movement=listdirect[pos]
        x=P_V[i][0]
        y=P_V[i][1]
        x,y = move(G,P,I,movement,nbr_case,x,y,P_V)
        #del P_V[i]
        G[x][y]= virus
        P_V[i][0]=x
        P_V[i][1]=y
        
def move(G,P,I,movement,nbr_case,x,y,P_V):
    loc=0 # car pas de repop virus
    if G[x][y] == virus:
        pos = 1
    else:
        pos = 2
    G[x][y]=" " #remplacer l'ancienne position par une case vide
    x_step=0
    y_step=0
    if movement == "s":
        y_step=1
    elif movement == "z": 
        y_step = -1
    elif  movement == "q":
        x_step = -1
    elif  movement == "d":
        x_step = 1        
    for i in range(nbr_case):
        y=y+(y_step)
        x=x+(x_step)
        if  test_grid(x,y,G) == False or G[x][y] == wall: # pas sortir de la grille ou un mur
            x,y = reculer(x,y,x_step,y_step)
            break
        elif G[x][y] == ATP: #ramassage des ATP
            if pos == 2 :
                power_up(I) 
                pop(1,ATP,loc) 
                G[x][y] = " " 
    while G[x][y] == virus or G[x][y] == 0 or G[x][y] == ATP: #la dernière position ne peux pas être un virus
        x,y = reculer(x,y,x_step,y_step)
    return x,y
    

#def movement_player():

    
def reculer(x,y,x_step,y_step):
    y=y-(y_step)
    x=x-(x_step)
    return x,y

def test_grid(x,y,G):
    if y > len(G)-1 or y < 0 or x > len(G)-1 or x < 0:
        return False
    return True
    
def drugs_inventory(I):#médicament=bombe
    i=0
    print "\nInventory\n"
    print "        Médicament       --> Portée"
    while i<4:
        print  "[",i+1,"]"," ",inventory[i][0]," --> ",inventory[i][1]
        i=i+1
    print "[ 0 ]   Retour au menu"
    tmp=raw_input("Quel est votre choix ?")
    if tmp == "0":
        exit
    if tmp == "1":
       pop = random.randint(0,3)
       inventory[0] = dinventory[pop]
    if tmp == "2":
       pop = random.randint(0,3)
       inventory[1] = dinventory[pop]
    if tmp == "3":
       pop = random.randint(0,3)
       inventory[2] = dinventory[pop]
    if tmp == "4":
       pop = random.randint(0,3) 
       inventory[3] = dinventory[pop]


def power_less(I):
    i = 0
    while i < 4:
        inventory[i][1]=inventory[i][1]-1
        if inventory[i][1] < 0 :
            inventory[i][1] = 0 
        i = i + 1

def power_up(I):
    i = 0
    while i<2:
        tmp=random.randint(0,3)
        inventory[tmp][1]=inventory[tmp][1]+1
        if inventory[tmp][1]>8:
            inventory[tmp][1]=8
        i = i + 1

def explode(G,a):
    global nb_vir
    x=position[0]
    y=position[1]+1
    size1=inventory[a][1]//2
    size2=inventory[a][1]-size1
    S=[size1,size2]
    rand1=random.randint(0,1)
    rand2=inventory[a][1]-S[rand1]
    i=0
    j=0
    while i<S[rand1]:
        if y>9:
            break
        if G[x][y]== virus :
            G[x][y]=' '
            nb_vir=nb_vir-1
        #G[x][y]='B' #test peter les mur et size (cheat des devs)
        y=y+1
        i=i+1
    y=position[1]-1
    while j<rand2:
        if y<0:
            break
        if G[x][y]=="\x1b[31;1mV\x1b[37;1m":
            G[x][y]=' '
            nb_vir=nb_vir-1
        #G[x][y]='H' #test peter les murs et size (cheat des devs)
        y=y-1
        j=j+1
    if nb_vir ==0:
        os.system("clear")
        print " __    __  _____   _   _        _          __  _   __   _  "
        print " \ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
        print "  \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
        print "   \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
        print "   / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
        print "  /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| "
        

        
def easy(grid):
    listx=[2,7,4,0,4,1,6,3,8,2]
    listy=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]=wall


#END OF GAME

def lose(I):
    x=0
    for i in I:
        if i[1]==0:
            x=x+1
    if x==4:
        os.system("clear")
        print "    __    __  _____   _   _        _       _____   _____   _____  "
        print "    \ \  / / /  _  \ | | | |      | |     /  _  \ /  ___/ | ____| "
        print "     \ \/ /  | | | | | | | |      | |     | | | | | |___  | |__   "
        print "      \  /   | | | | | | | |      | |     | | | | \___  \ |  __|  "
        print "      / /    | |_| | | |_| |      | |___  | |_| |  ___| | | |___  "
        print "     /_/     \_____/ \_____/      |_____| \_____/ /_____/ |_____| "

        
def menu(lol):
    print "====================================== Virus Killer ======================================="
    print "\n"
    print "[1] pour vous déplacer"
    print "[2] pour déposer un médicament"
    print "[0] pour quitter"
    print "\n"
    print "==========================================================================================="
 
def commandes(nb):
    os.system("clear")
    easy(grid)
    pop(8,ATP,location_virus) 
    pop(4,virus,location_virus) # 4 = number of Virus
    while nb != 0:
        print_grid(grid)
        menu(0)
        nb=raw_input() 
        if nb == "1":
            power_less(inventory)
            move_player(grid,location_player,inventory,location_virus)
            move_virus(grid,location_player,inventory,location_virus)
            print inventory
            lose(inventory)
        elif nb == "2":
            os.system("clear")
            print_grid(grid)
            drugs_inventory(inventory)
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            os.system("clear")
            print "ERREUR : mauvaise valeur"
            

######## MAIN ########

dinventory=[["Bombe nucléaire",8],["Grande bombe",6],["Moyenne bombe",4],["Petite bombe",2]] 
inventory=[["Bombe nucléaire",8],["Grande bombe",6],["Moyenne bombe",4],["Petite bombe",2]] 

grid=[]

location_player=[] #position du joueur
location_virus=[]

location_player.append(0)
location_player.append(0)

wall="\x1b[30;1mW\x1b[37;1m"
perso="\x1b[33;1m0\x1b[37;1m" 
virus="\x1b[31;1mV\x1b[37;1m"
ATP="\x1b[32;1mA\x1b[37;1m"

create_grid(grid)

#Initialisation  
#le joueur est matérialisé par un 0 sur la grille
grid[location_player[0]][location_player[1]]= perso #position initiale définie x=0 ;y=0

os.system("clear")

print "\x1b[32;1m _     _   _   _____    _   _   _____        _   _    _   _       _       _____   _____   "
print "\x1b[32;1m| |   / / | | |  _  \  | | | | /  ___/      | | / /  | | | |     | |     | ____| |  _  \  "
print "\x1b[32;1m| |  / /  | | | |_| |  | | | | | |___       | |/ /   | | | |     | |     | |__   | |_| |  "
print "\x1b[32;1m| | / /   | | |  _  /  | | | | \___  \      | |\ \   | | | |     | |     |  __|  |  _  /  "
print "\x1b[32;1m| |/ /    | | | | \ \  | |_| |  ___| |      | | \ \  | | | |___  | |___  | |___  | | \ \  "
print "\x1b[32;1m|___/     |_| |_|  \_\ \_____/ /_____/      |_|  \_\ |_| |_____| |_____| |_____| |_|  \_\ "

print "\n"
print "\n"

print "[1] START"
print "[2] EXIT"
rep=input()
commandes(rep)

