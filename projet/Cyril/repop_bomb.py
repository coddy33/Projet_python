#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur

import sys
import os
import random
#from energy import* 

#Create Grid

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


                
#Movment Player
#Régler le probleme out of range quand sort de la grille -> Ok
#code dupliqué pour la gestion d'erreur out of range
#bug déplacement, a chaque fois que le joueur se déplace, perte durabilité des bombes même si il a fait un déplacement dans un mur

def move(G,P):
    movement = raw_input("où voulez-vous aller ?")
    tmp=[]
    x=P[0]
    y=P[1]
    G[x][y]=" " #remplacer l'ancienne position par une case vide
    if movement == "d":#right
        right=input("de combien de cases voulez-vous vous déplacer ?")
        for i in G[x]:
            if i == "W":
                nb=G[x].index(i)
                tmp.append(nb)
        print x+right
        for i in tmp:
            if i >= x+right:
                print "Erreur"
                break
        if x+right >=10 :
            os.system("clear")
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        elif G[x+right][y] == "W": #pour ne pas s'arrêter sur un mur -> simplifier au dessus
            print "Vous ne pouvez pas traverser une membrane"
        else:
            x = x+right
    elif movement == "q":#left
        left=input("de combien de cases voulez-vous vous déplacer ?")
        if x-left <= 0 :
            os.system("clear")
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        if G[x-right][y] == "W":
            print "Vous ne pouvez pas traverser une membrane"
        else:    
            x = x-left
    elif movement == "s":#backward
        backward=input("de combien de cases voulez-vous vous déplacer ?")
        if y+backward <= 0 :
            os.system("clear")
            print "Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:    
            y = y+backward
    elif movement == "z":#foreward
        foreward=input("de combien de cases voulez-vous vous déplacer ?")
        if y-foreward <= 0 :
            os.system("clear")
            print "Erreur : Vous ne pouvez-pas sortir de l'espace cellulaire!"
        else:
            y = y-foreward
    else:
        os.system("clear")
        print "MAUVAIS DEPLACEMENT - UTILISEZ LES COMMANDES DE DEPLACEMENT Z Q S D"
    G[x][y]=0 # 0=le symbole qui matérialise le personnage dans la grille
    P[0]=x
    P[1]=y

def drugs_inventory():#médicament=bombe
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
    i=0
    while i<4: # A chaque fois que le personnage appelle cette fonction on perd un de portée sur toutes les bombes
        inventory[i][1]=(inventory[i][1])-1
        i=i+1
  
def energy(grid):
    for i in range(8):
        r=0    
        x=random.randint(0,9)
        listtmp=grid[x]
        while r==0:
            y=random.randint(0,9)
            if listtmp[y]!="W" and listtmp[y] !=0 and listtmp[y]!="A":
                grid[x][y]="A"
                break
            if listtmp[y]=="W" or listtmp[y]==0 or listtmp[y]=="A":
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
            
def easy(grid):
    listx=[2,7,4,0,4,1,6,3,8,2]
    listy=[0,1,2,3,4,5,6,7,8,9]
    for i in range(10):
        grid[listx[i]][listy[i]]="W"

#END OF GAME
#Essayer de mettre les deux dans une fonction

def win(): #pas encore utilisé
    print " __    __  _____   _   _        _          __  _   __   _  "
    print " \ \  / / /  _  \ | | | |      | |        / / | | |  \ | | "
    print "  \ \/ /  | | | | | | | |      | |  __   / /  | | |   \| | "
    print "   \  /   | | | | | | | |      | | /  | / /   | | | |\   | "
    print "   / /    | |_| | | |_| |      | |/   |/ /    | | | | \  | "
    print "  /_/     \_____/ \_____/      |___/|___/     |_| |_|  \_| "

def lose(I):
    if len(I) == 0:
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
    spawn_virus(grid)
    energy(grid)
    
    print grid[0][3]
    while nb != 0:
        print inventory
        print len(inventory)
        print_grid(grid)
        menu(0)
        nb=raw_input() 
        if nb == "1": #player movement
            #location(grid,position)
            power_less(inventory)
            move(grid,position)
            lose(inventory)
        elif nb == "2":
            os.system("clear")
            print_grid(grid)
            drugs_inventory()
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
            

######## MAIN ########
grid=[]

dinventory=[["Bombe nucléaire",8],["Grande bombe",6],["Moyenne bombe",4],["Petite bombe",2]] 
inventory=[["Bombe nucléaire",8],["Grande bombe",6],["Moyenne bombe",4],["Petite bombe",2]] 



position=[]

position.append(0)
position.append(0)


create_grid(grid)

#Initialisation  
#le joueur est matérialisé par un 0 sur la grille
grid[position[0]][position[1]]=0 #position initiale définie x=0 ;y=0

os.system("clear")

print " _     _   _   _____    _   _   _____        _   _    _   _       _       _____   _____   "
print "| |   / / | | |  _  \  | | | | /  ___/      | | / /  | | | |     | |     | ____| |  _  \  "
print "| |  / /  | | | |_| |  | | | | | |___       | |/ /   | | | |     | |     | |__   | |_| |  "
print "| | / /   | | |  _  /  | | | | \___  \      | |\ \   | | | |     | |     |  __|  |  _  /  "
print "| |/ /    | | | | \ \  | |_| |  ___| |      | | \ \  | | | |___  | |___  | |___  | | \ \  "
print "|___/     |_| |_|  \_\ \_____/ /_____/      |_|  \_\ |_| |_____| |_____| |_____| |_|  \_\ "

print "\n"
print "\n"

print "[1] START"
print "[2] EXIT"
rep=input()
commandes(rep)

#print l'inventaire dans le menu ?
#régler les os. clear
#faire la fonction pour perdre la partie