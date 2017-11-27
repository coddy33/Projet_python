#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation Python - Virus killer
# JUNG Frédéric
# DOURTHE Cyril
# THOUVENIN Arthur

import sys
import os
import random

def create_grid(grid):#Create Grid
    for i in range(10):
        list=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        grid.append(list)

def print_grid(grid,I):
    print "\n"
    print "----------- ","\x1b[33;1mVIRUS KILLER","\x1b[37;0m --------------"
    print "\x1b[30;1m+---+---+---+---+---+---+---+---+---+---+\x1b[37;1m"
    y=0
    while y<=9:
        x=0
        for h in range(9):
            print "\x1b[30;1m|\x1b[37;1m",grid[x][y],
            x=x+1
        print "\x1b[30;1m|\x1b[37;1m",grid[x][y],"\x1b[30;1m|\x1b[37;1m"
        print"\x1b[30;1m+---+---+---+---+---+---+---+---+---+---+\x1b[37;1m"
        y=y+1
    print_inventory(I)

def speech():
    star="\x1b[33;1m"u"\u2605""\x1b[37;1m"
    print """
=====================================================================================
|                                                                                   |
|                                ╓▄ª▀╙▀╙▀▀%w▄;                                      |
|                             ▄A▀             └▀▀v▄                                 |
|                          ╓A▀                     └█                               |    Welcome warrior,
|                         █                          ▌                              |
|                         ▌                          █                              |    You are in 2594, Humanity is in danger, recent advances in genetics, 
|                        ▐                           ▐⌐                             |    robotics, and technology are driving the world to extinction.
|                        █`└└""*"*ⁿⁿⁿ══════ⁿⁿª*ff**"?└▌                             |    
|                        █                            ▌                             |    A new virus appeared from nowhere, is name \x1b[31;1mSOVEREIGN!\x1b[37;1m""",virus,"""
|                       ,█¥═▄▄▄;,                 ,,;▄▌                             |
|                    ,═Γ█│\╙╕ ▀    ,▄⌠╙└└└└└└└└v▄ ,▄Ω<▌                             |    We detected 4 powerfull strains, if you succeed in destroying them, maybe humanity will have \x1b[33;1mHOPE!\x1b[37;1m
|                 ╓A▀ ,⌐▌,V╘▐▌       Q▀▀▀▄▄  .  ▄▀╙   ▌▄▄                           |
|              ,═▀  ,A  ▌Γ\ ▐▌       .│:       ▐     ▐└*w█▀▄▄                       |    For this mission you will have 4 anti-virus with different power to start.
|            ╓▀`   ╓┘   ▀▄╕ ▐= v                ▌≈=═Φ     ²Y▄▀¥▄                    |
|           ▄▌     ▌      ¥▄,▌   *      Γ       ╙¥  █         "w▀▀▄                 |    But on the field you will have \x1b[32;1mPower enhancer\x1b[37;1m : """,ATP,""" 
|          ▐▌▌     ▌     ╓▀▌ █    =     [x==l, ,Ü/ ╓▀            *▄▀W,              |    they will increase two of your anti-virus by 1.
|          ║ ╙▄    █    ▄¬█  └▌   ⌐ ,⌐`  ,-~ç  ,. '█               ╙╕╙█,            |
|          ║   ╕    █  A ▐⌐   ▀⌐  ⌐/   ç▄═¬═w╓=▄¬└ █                 ╙w▀▄           |    BUT above all, pay attention at the power of your anti-virus , 
|          ▐⌐   ╙▄   ▀█ ,▌     '▀ç"   ⌐'""ⁿ¬══─*  k█                   █┘           |    if they all fall to 0 we are all dead, nothing will stop him!
|           ▌     "w   ╙▀▄        ▀▄  ╞`¬ç   ,,╓┘ █▐Ö╗               ╓█╙▀W▄         |
|        ╓▄▀█       `\ç    ▀▀≡▄ç    ▀▄╘           ▌ █ ▀▄            ▄▀ "%, ▀▄       |
|      ▄▀   ▐▌         "═ç      `╙▀   "█▄        ,▌ ▐∩  █          █`     ▀  ▀█▄▄   |
|    ▄▀     █▀             "═w,   █     "▀▄▄▄▄▄≤▀▀   ▌   ▀       ,█ ▄▄≡Φ█▀▀▀└`      |
|  ▄█═"╙╙'" ▌ █                ⌐  ▌*≈¡      ,«"      █    █     ╓▀,▀     ▀▄ ┐       |
| ▄┘        ⌐  ▀▄             ▐  ▐=     -""¬         █     █   ╓▀ █        █ ╕      |
|▄¬        ▐     '▀▄,         ▐  ▐=                  ▌     █  ╓█  ▌         ▌ ⌐     |
|▌         ▐        `▀W▄      ▐  ▐▌▄                ▀     ▄  ,▌ ╙▄█         █ ▌     |
|         1**f▄      ╓¬═▀Φ▄    ▄  ▌ └ª═▄,        ╓A└    ╓▀   █    ▀▄        █ ▀     |
|         █   ▌      ▐   ▐⌐ ▀▄ ╙  █      └-""**"-     ▄▀¬   ▐ⁿ╩"│Ö▐^▌▄.ÜΩ╣]ó▄╫╫▄▄   |
|         ▀   *      └   '    ▀ * ╙                 ^┘               ▀▀*"╙▀▀└¬      |
|                                                                                   |
|                                  \x1b[33;1mGeneral Mike Hertz\x1b[37;1m                               |
|                                                                                   |
=====================================================================================
"""
    print """
Choose your level of difficulty :

[1] Easy     : better to begin againt \x1b[31;1mSOVEREIGN!\x1b[37;1m."
[2] Normal   : you may have guts...
[3] Hardcore : finally a real warrior, let me see your true nature as a hero!""",star,"""\n
[0] Leave."""

def pop(nb,mol,loc,G): #on defini le nombre de pop=nb ; puis quelle molecule doit pop=mol
    for i in range(nb):
        r=0
        loc_virus=[]
        while r==0:
            x=random.randint(0,9)
            y=random.randint(0,9)
            if test_grid_empty(x,y,G)==True:
                G[x][y]=mol
                if mol == virus:
                    loc_virus.append(x)
                    loc_virus.append(y)
                    loc.append(loc_virus)
                break
            if test_grid_empty(x,y,G)==False:
                continue

def move_player(G,P,I,P_V):#Movment Player
    movement = raw_input("Où voulez-vous aller ?")
    nbr_case=input("De combien de cases voulez-vous vous déplacer ?") # erreur possible si input string
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
                pop(1,ATP,loc,G)
                G[x][y] = " "
    while G[x][y] == virus or G[x][y] == perso or G[x][y] == ATP: #la dernière position ne peux pas être un virus
        x,y = reculer(x,y,x_step,y_step)
    return x,y

###test

def reculer(x,y,x_step,y_step):
    y=y-(y_step)
    x=x-(x_step)
    return x,y

def test_grid(x,y,G):
    if y > len(G)-1 or y < 0 or x > len(G)-1 or x < 0:
        return False
    return True

def test_grid_empty(x,y,G):
    if test_grid(x,y,G)==True and G[x][y]==' ' :
        return True
    return False

###le rendre plus esthétique

def print_inventory(I):
    i=0
    print "\x1b[30;1m\n=============  \x1b[37;0mInventory\x1b[30;1m  ===============\n"
    print "        Médicament       --> Portée"
    while i<4:
        print  "[",i+1,"]"," ",I[i][0]," --> ",I[i][1]
        i=i+1
    print "\x1b[37;0m\n"

#### voir try et except pour mauvais input

def drugs_inventory(I,G,P_J,P_V):#médicament=bombe
    tmp=input("Quel est votre choix ?")
    if tmp != 0 :
        explode(G,I,P_J,P_V,tmp-1)
        pop = random.randint(0,3)
        inventory[tmp-1] = dinventory[pop]
    if tmp == "0":
        exit

def power_less(I):
    i = 0
    while i < 4:
        I[i][1]=I[i][1]-1
        if I[i][1] < 0 :
            I[i][1] = 0
        i = i + 1
    lose(I)

def power_up(I):
    i = 0
    while i<2:
        tmp=random.randint(0,3)
        I[tmp][1]=I[tmp][1]+1
        if I[tmp][1]>8:
            I[tmp][1]=8
        i = i + 1

def explode(G,I,P_J,P_V,C):
    x= P_J[0]
    y= P_J[1]
    size_foreward = I[C][1]//2
    size_backward = I[C][1]-size_foreward
    S=[size_foreward,size_backward]
    rand1=random.randint(0,1)
    rand2=inventory[C][1]-S[rand1]
    step_foreward = 1
    step_backward = -1
    for i in range(size_foreward):#down
        y=y+step_foreward
        if  test_grid(x,y,G) == False or G[x][y] == wall: # pas sortir de la grille ou un mur
            break
        if G[x][y] == virus:
            #G[x][y]='B'
            depop_virus(x,y,P_V)
            G[x][y] = " "
    for i in range(size_backward):#up
        y=y+step_backward
        if  test_grid(x,y,G) == False or G[x][y] == wall: # pas sortir de la grille ou un mur
            break
        if G[x][y] == virus :
            #G[x][y]='F'
            depop_virus(x,y,P_V)
            G[x][y] = " "
        
def depop_virus(x,y,P_V):
    print x
    print y
    index = P_V.index([x,y])
    del P_V[index]

################################

def win(loc_virus):
    if len(loc_virus)==0:
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

def normal(grid):
    listx=[2,8,7,3,7,4,0,2,0,4,9,1,6,1,6,3,0,8,2,6]
    listy=[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]=wall

def hardcore(grid):
    listx=[2,8,3,6,7,1,4,7,0,2,9,0,4,5,7,1,3,9,1,6,7,3,4,5,6,0,8,9,2,6]
    listy=[0,0,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9]
    for i in range(len(listx)):
        grid[listx[i]][listy[i]]=wall

def lose(I):
    x=0
    for i in I:
        if i[1]==0:
            x=x+1
    if x==4:
        print """
                 __
            ,-~¨^  ^¨-,           _,
           /          / ;^-._...,¨/
          /          / /         /
         /          / /         /
        /          / /         /
       /,.-:''-,_ / /         /
       _,.-:--._ ^ ^:-._ __../
     /^         / /¨:.._¨__.;
    /          / /      ^  /
   /          / /         /
  /          / /         /
 /_,.--:^-._/ /         /
^            ^¨¨-.___.:^  
"""
        os.system("clear")
        print "    __    __  _____   _   _        _       _____   _____   _____  "
        print "    \ \  / / /  _  \ | | | |      | |     /  _  \ /  ___/ | ____| "
        print "     \ \/ /  | | | | | | | |      | |     | | | | | |___  | |__   "
        print "      \  /   | | | | | | | |      | |     | | | | \___  \ |  __|  "
        print "      / /    | |_| | | |_| |      | |___  | |_| |  ___| | | |___  "
        print "     /_/     \_____/ \_____/      |_____| \_____/ /_____/ |_____| "

def menu(L):
    print "============ Virus Killer ==============="
    print "\n"
    print "[1] pour vous déplacer"
    print "[2] pour déposer un médicament"
    print "[0] pour quitter"
    print "\n"
    print "========================================="

def commandes(level):
    a=0
    os.system("clear")
    level(grid)
    pop(nb_ATP,ATP,location_virus,grid)
    pop(nb_vir,virus,location_virus,grid) # 4 = number of Virus
    while a == 0:
        print_grid(grid,inventory)
        menu(0)
        nb=raw_input()
        if nb == "1":
            power_less(inventory)
            move_player(grid,location_player,inventory,location_virus)
            move_virus(grid,location_player,inventory,location_virus)
        elif nb == "2":
            drugs_inventory(inventory,grid,location_player,location_virus)
            os.system("clear")
            print_grid(grid,inventory)
        elif nb == "0":
            exit()
            #start()
        else:
            os.system("clear")
            print "You make a mistake, retry please..."

def print_title():
    os.system("clear")
    print """\x1b[32;1m     _     _   _   _____    _   _   _____        _   _    _   _       _       _____   _____   
    | |   / / | | |  _  \  | | | | /  ___/      | | / /  | | | |     | |     | ____| |  _  \  
    | |  / /  | | | |_| |  | | | | | |___       | |/ /   | | | |     | |     | |__   | |_| |  
    | | / /   | | |  _  /  | | | | \___  \      | |\ \   | | | |     | |     |  __|  |  _  /  
    | |/ /    | | | | \ \  | |_| |  ___| |      | | \ \  | | | |___  | |___  | |___  | | \ \  
    |___/     |_| |_|  \_\ \_____/ /_____/      |_|  \_\ |_| |_____| |_____| |_____| |_|  \_\ \x1b[37;1m"""
    print """\x1b[31;1m                 _                      _________                    _
               _dMMMb._              .adOOOOOOOOOba.              _,dMMMb_
              dP'  ~YMMb            dOOOOOOOOOOOOOOOb            aMMP~  `Yb
              V      ~"Mb          dOOOOOOOOOOOOOOOOOb          dM"~      V
                       `Mb.       dOOOOOOOOOOOOOOOOOOOb       ,dM'
                        `YMb._   |OOOOOOOOOOOOOOOOOOOOO|   _,dMP'
                   __     `YMMM| OP'~"YOOOOOOOOOOOP"~`YO |MMMP'     __
                 ,dMMMb.     ~~' OO     `YOOOOOP'     OO `~~     ,dMMMb.
              _,dP~  `YMba_      OOb      `OOO'      dOO      _aMMP'  ~Yb._
            <MMP'     `~YMMa_    YOOo   \x1b[37;1m@\x1b[31;1m  OOO  \x1b[37;1m@\x1b[31;1m   oOOP   _adMP~'      `YMM>
                          `YMMMM\`OOOo     OOO     oOOO'/MMMMP'
                  ,aa.     `~YMMb `OOOb._,dOOOb._,dOOO'dMMP~'       ,aa.
                ,dMYYMba._         `OOOOOOOOOOOOOOOOO'          _,adMYYMb.
               ,MP'   `YMMba._      OOOOOOOOOOOOOOOOO       _,adMMP'   `YM.
               MP'        ~YMMMba._ YOOOOPVVVVVYOOOOP  _,adMMMMP~       `YM
               YMb           ~YMMMM\`OOOOI`````IOOOOO'/MMMMP~           dMP
                `Mb.           `YMMMb`OOOI,,,,,IOOOO'dMMMP'           ,dM'
                  `'                  `OObNNNNNdOO'                   `'
                                        `~OOOOO~'         
    \x1b[37;1m"""
    print """
                                             ^
                                _______     ^^^
                               |xxxxxxx|  _^^^^^_
                               |xxxxxxx| | [][]  |
                            ______xxxxx| |[][][] |
                           |++++++|xxxx| | [][][]|      METROPOLIS
                           |++++++|xxxx| |[][][] |
                           |++++++|_________ [][]|
                           |++++++|=|=|=|=|=| [] |
                           |++++++|=|=|=|=|=|[][]|
                ___________|++HH++|  _HHHH__|   _________   _________  _________
                         _______________   ______________      ______________
                __________________  ___________    __________________    ____________"""
    print "\x1b[32;1m =============================================================================================\x1b[37;1m"
    print "\n"
    print "\n"
    print "[1] START"
    print "[0] EXIT"

def exit():
    os.system("clear")
    print "Are you sure?"
    print "[1] YES"
    print "[0] NO"
    choice=input()
    if choice==1:
        print "Goodbye warrior!"
        sys.exit()

def difficulty():
    lvl=raw_input()
    if lvl=="0":
        exit()
    elif lvl=="1":
        commandes(easy)
    elif lvl=="2":
        commandes(normal)
    elif lvl=="3":
        commandes(hardcore)
    else:
        print "You make a mistake, retry please..."
        #gestion d'erreur
def start():
    print_title()
    rep=raw_input()
    while rep != 0:
        os.system("clear")
        if rep=="1":
            speech()
            difficulty()
        if rep==0:
            exit()
        else:
            print "You make a mistake, retry please..."
            continue




######## MAIN ########

nb_ATP=8
nb_vir=4
dinventory=[["Bombe nucléaire",8],["Grande bombe",6],["Moyenne bombe",4],["Petite bombe",2]]
inventory=[["Bombe nucléaire",8],["Grande bombe",6],["Moyenne bombe",4],["Petite bombe",2]]
grid=[]
location_player=[] #position du joueur
###
location_virus=[]
###
location_player.append(0)
location_player.append(0)
wall="\x1b[30;1m"u"\u25a9\x1b[37;1m"
perso="\x1b[33;1m"u"\u263b\x1b[37;1m"
virus="\x1b[31;1m"u"\u2620\x1b[37;1m"
ATP="\x1b[32;1m"u"\u2622\x1b[37;1m"
create_grid(grid)

#Initialisation
#le joueur est matérialisé par un 0 sur la grille
grid[location_player[0]][location_player[1]]= perso #position initiale définie x=0 ;y=0

start()

