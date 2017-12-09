#!/usr/bin/env python
#-*- coding: utf-8 -*-

adn = "agccgtaggctatttcgacgcaa"
#print(adn)
#print(len(adn) ) #longueur de la string
#print(adn[0]) #lettre en position 0
adn =  "tga" + adn #ajoute au début
adn = adn + "ccc" #ajoute à la fin
#print( len(adn) )
#print adn
#print "==========================="
#print "\n"



def mystere(prot):
    nb_cys = 0
    for aa in protein:
        if aa == "C" :
            nb_cys = nb_cys + 1
    return nb_cys

protein = "CVAPGPMCAWCDSTAC"
num = mystere(protein)
#print "il␣y␣a␣" , num , "␣Cysteine(s)"
#print "==========================="
#print "\n"


#Exercice 2.2.1: En vous inspirant des exercices précédents, écrivez la fonction isDNA(seq) qui retourne True si la séquence d’ADN (une String) contient uniquement des “A”, des “T”, des “C” et des “G”.


def isDNA(string):
    for nuc in string:
        if nuc != "a" and nuc != "t" and nuc != "c" and  nuc != "g":
            return False


adn = "agccgtaggctatttcgacgcaa"
adn1 = "agccgtaggctatttcgacegcaa"
#print isDNA(adn)
#print isDNA(adn1)

#Exercice 2.2.2: Écrire une fonction countPro(seqProt) qui retourne le nombre de prolines (code à une lettre “P”) dans une séquence protéique.

def countPro(seqProt):
    nbPro=0
    for aa in seqProt:
        if aa == "p" or aa == "P":
            nbPro=nbPro+1
    return nbPro

seq="kbdchkzepjhsdjpkjhhzgjhzpPkhcbjzhbp"
#print countPro(seq)
            
#Exercice 2.2.3: Écrire une fonction countAll(seqProt,symbol) qui retourne le nombre d’acides aminés correspondant au code à une lettre dans une séquence protéique.

def countAll(seqProt,symbol):
    nb=0
    for aa in seqProt:
        if aa == symbol or aa == symbol:
            nb=nb+1
    return nb

seq='MVHLSAEEKEAVLGLWGKVNVDEVGGEALGRLLVVYPWTQ'
#print countAll(seq,'P') # 1
#print countAll(seq,'V') # 7

#Exercice 2.2.4: Écrire une fonction oneWord(seq,start,wlen) qui extrait un mot de longueur wlen à la position start.

def oneWord(seq,start,wlen):
    return seq[start:wlen+start]
   
seq='ABCDEFGHIJKLM'
#s = oneWord(seq,4,5) # "EFGHI"
#print s

#Exercice 2.2.5: Écrire une fonction countWord(seq,word) qui compte le nombre de mots word présent dans la chaîne de caractères seq (String).

def countWord(seq,word):
    wlen = len(word)
    count=0
    for i in range(len(seq)):
        if oneWord(seq,i,wlen) == word:
            count=count+1
    return count

phrase='CTGATGTTCCATTACCAGTACAACAAACTATGATTCCATTACCAGTACA'
num = countWord(phrase,'ATG') 
num2 = countWord(phrase,'TGA')
#print "le nombre de ATG est de : " , num
#print "le nombre de ATG est de : " , num2

#Exercice 2.2.6: Écrire une fonction isCodonStart(seq,pos) qui retourne true si le codon dans la séquence seq à la position pos est un codon start ATG.

def isCodonStart(seq,pos):
    wlen = len("ATG")
    if oneWord(seq,pos,wlen) == "ATG":
        return True

seq='CTGATGTTCCATTACCAGTACAACAAACTATGATTCXXCATTACCAGTACA'
flag = isCodonStart(seq,3) # True
#print flag

#Exercice 2.2.7: Écrire une fonction isCodonStop(seq,pos) qui retourne truesi le codon dans la séquence seq à la position pos est un codon stop: TAA ou TAG ou TGA.

def isCodonStop(seq,pos):
    wlen = len("XXX")
    if oneWord(seq,pos,wlen) == "TAA" or oneWord(seq,pos,wlen)== "TAG" or oneWord(seq,pos,wlen)== "TGA":
        return True

seq1='CTGATGTTCCATTACCAGTACAACAAACTXATGATTCCATTACCAGTACA'
seq='CTGATGTTCCATTACCAGTACAACAAACTATGATTCCATTACCAGTACA'
flag = isCodonStop(seq,30) # True
flagi=isCodonStop(seq1,30) # False
#print flag
#print flagi

#Exercice 2.2.8: Écrire une fonction isGene(seq) qui retourne true si la séquence contient un codon start et un codon stop.

def isGene(seq):
    x=0
    y=0
    for i in range(len(seq)):
        if isCodonStart(seq,i*3)== True :
            x=1
        if isCodonStop(seq,i*3)== True:
            y=1
    if x == y:
        return True
        
seq='CTGATGTTCCATTACCAGTACAACAAACTATGATTCCATTACCAGTACA'
seq1="ATGXXTAAXXXX"
flag = isGene(seq) # True
flagi = isGene(seq1)
#print flag
#print flagi

#Traduire une séquence
'''
def translate(seq):
    translated_ORF=[]
    for i in range(len(seq),3):
        tmp=[]
        tmp.append(seq[i])
        tmp.append(seq([i+1])
        tmp.append(seq([i+2])
        print tmp
    return translated_ORF
'''


#Exercice 2.2.9: Écrire une fonction isGene3(seq) qui retourne true si la séquence contient un codon start et un codon stop pour les 3 cadres de lecture.

def isGene3(seq):
    for i in range(len(seq)):
        if isCodonStart(seq,i) == True : #return True
            frame1 = i%3
            j=i
            for j in range(len(seq)):#faire commencer après le start
                if isCodonStop(seq,j) == True :
                    frame2 = 1%3
                    if frame2 == frame1:
                        return True
           




#print isGene3(seq1)

##############################################PROJECT##############################################
"""
def isCodonStart(seq,pos,L):
    wlen = len("XXX")
    for i in L:
        if oneWord(seq,pos,wlen) == i:
            return True

def isCodonStop(seq,pos,L):
    wlen = len("XXX")
    for i in L :
        if oneWord(seq,pos,wlen) == i:
            return True
"""

def find_ORF(seq):
    list=[]
    for i in range(len(seq)):
         if isCodonStart(seq,i) == True :
            for j in range(i,len(seq)-i):
                if isCodonStop(seq,j) == True :
                    if i%3 == j%3:
                        lenORF=len(seq[i:j+3])
                        if lenORF > treshold:
                            list.append(seq[i:j+3])
                            return list

#seq='TGA TGT TCC ATT ACC AGT ACA ACA AAC TAT GAT TCC ATT ACC AGT ACA'
#seq='TG ATG TTC CAT TAC CAG TAC AAC AAA CTA TGA TTC CAT TAC CAG TAC A'
           
seq='TGATGTTCCATTACCAGTACAACAAACTATGATTCCATTACCAGTACA'
#print "===========", seq[4:10]
flag = isGene3(seq) # True
print flag                    
"""           
def seq_ORF(seq,pos1,pos2):
    return seq[]"""
