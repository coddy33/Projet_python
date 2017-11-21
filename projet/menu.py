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


"""
#Localisation du joueur
#vraiment nécessaire ? car initialisation coordonnées connus 
def location(G,P):
    x=0
    y=0
    for j in range(len(G)): #chercher la position du joueur
        for i in G[j]: #mettre aussi dans une boucle for pour le G[j]
            if i == 0:
                y = G[j].index(0) # coordonées en y
                x = j #coordonées en x
                P.append(x)
                P.append(y)
"""
                
#Movment Player
#Régler le probleme out of range quand sort de la grille -> Ok
#code dupliqué pour la gestion d'erreur out of range
#bug déplacement, a chaque fois que le joueur se déplace, perte durabilité des bombes même si il a fait un déplacement dans un mur

def move(G,P):
    movement = raw_input("où voulez-vous aller ?")
    nbr_case=input("de combien de cases voulez-vous vous déplacer ?") # erreur possible si input string
    x=P[0]
    y=P[1]
    tmp_x=x #ancienne position en x
    tmp_y=y #ancienne position en y
    G[x][y]=" " #remplacer l'ancienne position par une case vide    
    if movement == "s":#backward
        step=1
    elif movement == "z":#foreward
        step=-1
    elif movement == "d":#right
        step=1
    elif movement == "q": #left
        step=-1
    else:
        os.system("clear")
        print "MAUVAIS DEPLACEMENT - UTILISEZ LES COMMANDES DE DEPLACEMENT Z Q S D"
    if movement == "s" or  movement =="z":
        for i in range(nbr_case):
            if G[x][y+(step)] == wall: #wall
                break
            elif tmp_y+nbr_case >=10 and tmp_y-nbr_case > 0 :
                break
            else:
                y=y+(step)
        if G[x][y] == virus: #virus
            y=y-(step)
    if movement == "d" or movement == "q" :
        for i in range(nbr_case):
            if tmp_x+nbr_case >= 10 and tmp_x-nbr_case > 0: 
                break
            elif  G[x+(step)][y] == wall: #position d'un mur
                break
            else:
                x=x+(step)
        if G[x][y] == virus: #position d'un virus
            x=x-(step)
    os.system("clear")
    G[x][y]= perso # 0=le symbole qui matérialise le personnage dans la grille
    P[0]=x
    P[1]=y

def drugs_inventory(I):#médicament=bombe
    print "\n"
    print "Medicament       Portée"
    for w in I :
        print w[1], "   ", w[0], "---------->" ,"[" ,w[2], "]"
    print "\n"
    rep=raw_input("Voulez-vous utiliser un médicament ?")
    if rep == "yes":
        print "\n"
        tmp=input("Quelle médicament voulez vous utiliser ?")
        I[tmp][1]=(I[tmp][1])-1
        #rajouter un return des dégats
        if I[tmp][1] == 0:
            del I[tmp] #supprime un élément de l'inventaire
    else :
        print "Retour au menu..."

def power_less(I):
    tmp=0
    for i in I: # A chaque fois que le personnage appelle cette fonction on perd un de portée sur toutes les bombes
        i[2]=i[2]-1
    for i in I: # A chaque fois que la portée passe à 0 le médicament=bombe est supprimé
        if i[2] == 0:
            del I[tmp]
        else:
            tmp=tmp+1
            
#def use_energy():

def pop(nb,mol): #on defini le nombre de pop=nb ; puis quelle molecule doit pop=mol
    for i in range(nb):
        r=0    
        x=random.randint(0,9)
        listtmp=grid[x]
        while r==0:
            y=random.randint(0,9)
            if listtmp[y]!=wall and listtmp[y] !=0 and listtmp[y]!=ATP and listtmp[y]!=virus:
                grid[x][y]=mol
                break
            if listtmp[y]==wall or listtmp[y]==0 or listtmp[y]==ATP or listtmp[y]==virus:
                continue

def easy(grid):
    listx=[2,7,4,0,4,1,6,3,8,2]
    listy=[0,1,2,3,4,5,6,7,8,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]=wall  


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
    pop(nb=8,mol=ATP)
    pop(nb=4,mol=virus)#pop Virus
    while nb != 0:
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
            drugs_inventory(inventory)
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
            

######## MAIN ########

Items={"Bombe_nucleaire":8,"Grande_bombe":6,"Moyenne_bombe":4,"Petite_bombe":2}

inventory=[["ATP",1,3],["ATP",1,2],["ATP",1,1]]

Bombe_nucleaire=["A",1,8]
Grande_bombe =["B",1,Items["Grande_bombe"]]
Moyenne_bombe=["C",1,Items["Moyenne_bombe"]]
Petite_bombe=["D",1,Items["Petite_bombe"]]

#initialisation 4 bombes
inventory.append(Bombe_nucleaire)
inventory.append(Grande_bombe)
inventory.append(Moyenne_bombe)
inventory.append(Petite_bombe)

grid=[]

position=[]

position.append(0)
position.append(0)

wall="\x1b[30;1mW\x1b[37;1m"
perso="\x1b[33;1m0\x1b[37;1m" 
virus="\x1b[31;1mV\x1b[37;1m"
ATP="\x1b[32;1mA\x1b[37;1m"

create_grid(grid)

#Initialisation  
#le joueur est matérialisé par un 0 sur la grille
grid[position[0]][position[1]]=0 #position initiale définie x=0 ;y=0

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

#print l'inventaire dans le menu ?
#régler les os. clear
#faire la fonction pour perdre la partie
