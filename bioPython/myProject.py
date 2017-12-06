#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Projet de programmation BioPython
# BLASQUIZ Julie
# JUNG Frédéric
# THOUVENIN Arthur



import myBio as bio
import myProject as proj
import codecs
import sys
import re

#############################standard code 1
listcode=['nothing']
AAs   ='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts='---M------**--*----M---------------M----------------------------'
Base1 ='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2 ='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3 ='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
list1=[AAs,Starts,Base1,Base2,Base3]
listcode.append(list1)

#############################The Vertebrate Mitochondrial Code 2
AAs   ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG'
Starts='----------**--------------------MMMM----------**---M------------'
Base1 ='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2 ='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3 ='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
list1=[AAs,Starts,Base1,Base2,Base3]
listcode.append(list1)
##############################The Yeast Mitochondrial Code 3
AAs   ='FFLLSSSSYY**CCWWTTTTPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts='----------**----------------------MM----------------------------'
Base1 ='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2 ='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3 ='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
list1=[AAs,Starts,Base1,Base2,Base3]
listcode.append(list1)

def error():
    '''This function control error through the programm, like input errors.

    Description:
        This function manage erros through try and except that try something
        and if is not working this return a message of error instead of just crash the programm.
    Args:
        No arguement needed.
    Return:
        nb:number choosen by USER
        and print "Wrong value..." if it's wrong.
    '''
    i=1
    while i !=0:
        try :
            nb=input()
            return nb
        except NameError: # if input = string
            print "Wrong NCBI_ID..."
        except SyntaxError: # for special character
            print "Wrong NCBI_ID..."

def getGeneticCode(nb):
    dicocode={}
    for i in range(len(listcode[nb][0])):
        codon=listcode[nb][2][i]+listcode[nb][3][i]+listcode[nb][4][i]
        dicocode.update({codon:listcode[nb][0][i]})
    print(dicocode)
    return dicocode

def getGeneticCodeStart(nb):
    dicocodestart={}
    for i in range(len(listcode[nb][1])):
        if listcode[nb][1][i]!='-' and listcode[nb][1][i]!='*':
            codon=listcode[nb][2][i]+listcode[nb][3][i]+listcode[nb][4][i]
            dicocodestart.update({codon:listcode[nb][1][i]})
    print (dicocodestart)
    return dicocodestart

def getGeneticCodeStop(nb):
    dicocodestop={}
    for i in range(len(listcode[nb][1])):
        if listcode[nb][1][i]!='-' and listcode[nb][1][i]!='M':
            codon=listcode[nb][2][i]+listcode[nb][3][i]+listcode[nb][4][i]
            dicocodestop.update({codon:listcode[nb][1][i]})
    print(dicocodestop)
    return dicocodestop

getGeneticCodeStop(0)
getGeneticCodeStart(0)
getGeneticCode(0)


#####################################################################################################################################################################################################################

def findORF(seq, treshold, codeTable):######demander treshold
    '''This function is the main function of our script this function call all other to make the programm work

    Description:

    Args:
        seq: a nucleic sequence
        treshold: the minimumof ORF length in bp
        codeTable: a genetic code table

    Return:
        list of ORFs

    '''
    L=getGeneticCode(codeTable)
    start=L[2]
    print start
    stop=L[1]
    print stop
    list_ORF=[]
    list_translated_ORF
    for i in range(len(seq)):
        if bio.isCodonStart(seq,i) == True :
            for j in range(i,len(seq)-i):
                if bio.isCodonStop(seq,j) == True :
                    if i%3 == j%3:
                        lenORF=len(seq[i:j+3])
                        if len(ORF) > treshold:
                            list.append(seq[i:j+3])

###########################################################"""


def translate(listorf):
    tmp=listorf
    j=0
    for i in tmp:#i = 1 orf
        





def getLengths(orf_list):
    '''This function determine the length of ORFs

    Desciption:
        This function use the list of ORFs and use length of each element to know lengths

    Args:
        orf_list: list of ORF produce by find ORF function

    Return:
        Two list:
            - First list where sizes are in bp(sizelistbp)
            - Second list where sizes are in aa(sizelistaa)
    '''
    sizelistbp=[]
    sizelistaa=[]
    for i in orf_list:
        size=len(i)
        sizelist.append(size)
        sizeaa=size/3
        sizelistaa.append(sizeaa)
    return sizelistbp,sizelistaa

#a verifier
def getLongestORF(orf_list):
    for i in orf_list:
        result = getLengths(i)
    x=result[0]
    for i in result:
        if i>x:
            x=i
    maxi=x
    indice = []
    for i in result:
        if i==maxi:
            indice.append(i)
    return orf_list[indice]

def getTopLongestORF(orf_list,value):
    topvalues=[]
    tmp=orf_list
    s=len(orf_list)
    s=(1-value)*s
    while s>0:
        y=getLongestORF(tmp)
        topvalues.append(y)
        tmp.pop(tmp.index(y))
        s=s-1




def writeCSV(filename, separator):#revoir
    '''This function allow current programm to save in file which the name is choosen

    Description:
        In this function we open a file whi name is choose by the user and then we write dictionnary

    Args:
        filename: file name
        separator: separator for save objects in filename

    Return:
        J'en sais rien########################
    '''
    file=codecs.open(filename,"w",encoding="utf-8")
    file.write(':')
    for key in dict.keys():####################revoir le dict
        file.write(key)
        file.write(separator)
    file.write('\n')
    file.write('>')
    for values in dict.values():###########revoir le dict
        file.write(values)
        file.write(separator)

def readCSV(filename, separator,data):#revoir
    '''This function allow current programm to load a file

    Description:
        User choose file to load and then this functio open file and read line by line, first line = listkey, second line = listvalues
        Then we make a dictionnary from those lists.

    Args:
        filename: file name
        separator: separator for load objects in filename

    Return:
        ####### Dictionnary of ORFs.
    '''
    file=codecs.open(filename,"r",encoding="utf-8")
    listkey=[]
    listvalues=[]
    for line in file.readlines():
        if not line:
            break
        if line.startswith(':'):
            listkey=line.split(separator)
        if line.startswith('>'):
            listvalues=line.split(separator)
    if len(listkey)!=len(listvalues):
        print 'Corrupted save file.'
    for i in listkey:
        n=0
        dict[i]=listvalues[n]######## revoir le dict
        n=n+1
    return dict################revoir dict

def compare(orflist1,orflist2):###############same size?+revoir
    '''This function compare two list of orf and returns orfs which are present in those two lists.
    Desciption:
        In this function we use each element i orflist1 to see if they are in orflist2.

    Args:
        orflist1: list 1 of orfs
        orflist2: list 2 of orfs

    Return:
        this function return a list of all similar genes.
    '''
    same=[]
    for i in orflist1:
        if i in orflist2:
            same.append(i)
    return same

def readFlatFile(filename):
    '''This function read a FlatFile

    Description:
        Here we open and then read a flat file and then store information in a variable which we return

    Args:
        filename : name of the file read

    Return:
        Return a string of all file read.
    '''
    file=codecs.open(filename,"r",encoding="utf-8")
    Flat=file.read()
    return Flat

def getFeatures(txt):
    '''This function gives features of a FlatFile read before by readFlatFile.

    Description: This function cut the string containing the flatfile to "ORIGIN" from "FEATURES" and return this part.

    Args:
        txt: a flatfile in a string.

    Return:
        tmp: a string cut from the flatfile.

    '''
    tmp=txt.partition("FEATURES")[2].partition("ORIGIN")[0]
    return tmp

def getGenes(txt):
    '''This function get genes caracteristics

    Desciption:
        This function find how many 'gene' are in the txt to fix the number of loop to take informations of each gene.
        We made a function register_gene() to take information of each gene.

    Args:
        txt: a string that contain a specific format and all genes

    Return:
        listdico: a list containing all dictionnary containning information about all genes.

    '''
    listdico=[]
    remove=txt.partition('gene  ')[0]
    txt=txt[len(remove):]
    tmp=txt##remove all before first gene
    length=tmp.count(' gene  ')#number of gene?
    firstg=tmp.partition('     gene            ')[0]#first gene
    listdico.append(register_gene(firstg))
    for i in range(length):
        firstg=tmp.partition('     gene            ')[0]
        tmp=tmp[len(firstg):]
        secondg=tmp.partition('     gene            ')[2].partition(' gene     ')[0]#all genes are taking back
        listdico.append(register_gene(secondg))
        tmp=tmp[len(secondg):]
    return listdico

def register_gene(tmp):
    '''This function take all information about only one gene in a string and take them in a dictionnary.

    Description:
        There is specific paragraph for information, so 7 data : start,stop,length,frame,name,protein,product
        And at list a paragraph to take all of information in a dictionnary.

    Args:
        tmp: a string containing only one gene.

    Return:
        dico: a dictionnary about gene and all of these information.
    '''
    ###############  start  ##################
    l=re.findall(r'\d+',tmp)
    start=int(l[0])
    ###############  stop  ##################
    stop=int(l[1])
    ###############  length  ##################
    length=stop-start
    ###############  frame  ###################
    fra=0
    if 'complement' in tmp:
        fra=-1
    else:
        fra=1
    value=start%3
    frame=fra*(value+1)
    ###############  name  ###################
    name=''
    name=tmp.partition('gene=\"')[2].partition('\"')[0]
    if name == '':
        name='unknow'
    ###############  protein  ##################
    protein=''
    protein=tmp.partition('/protein_id=\"')[2].partition('\"')[0]
    if protein=='':
        protein='xxx'
    ###############  product  ##################
    product=''
    product=tmp.partition('/product=\"')[2].partition('\"')[0]
    if product=='':
        product='unknown'
    ############################  DICT  #######################################"
    dico={'start':start,'stop':stop,'length':length,'frame':frame,'name':name,'protein':protein,'product':product}
    return dico
    '''
    print('frame',frame)
    print ('start',start)
    print ('stop',stop)
    print ('length',length)
    print ('name',name)
    print ('protein',protein)
    print ('product',product)
    '''

def readGenBank(filename):#description
    txt=readFlatFile(filename)
    register_general(txt)

def register_general(txt):#description
    ###############  description  ##################
    tmp=txt.partition('DEFINITION  ')[2].partition('\nACCESSION')[0]
    description=tmp
    ###############  type  ##################
    tmp=txt.partition('bp    ')[2].partition('     ')[0]
    typeda=tmp
    ###############  data  ##################
    tmp=txt.partition('ORIGIN')[2].partition('//')[0]
    data=tmp
    ###############  ID  ##################
    tmp=txt.partition('LOCUS       ')[2].partition(' ')[0]
    ID=tmp
    ###############  length  ##################
    tmp=txt.partition('LOCUS       ')[2].partition(' bp')[0]
    tmp=tmp.split(' ')
    leng=int(tmp[len(tmp)-1])
    ###############  gbtype  ##################
    tmp=txt.partition('/mol_type="')[2].partition('"\n')[0]
    gbtype=tmp
    ###############  organism  ##################
    tmp=txt.partition('ORGANISM  ')[2].partition('\n')[0]
    organism=tmp
    ###############  codeTableID  ##################
    tmp=''
    tmp=txt.partition('/transl_table=')[2].partition('\n')[0]
    if tmp=='':
        GeneticCode=1
    else:
        GeneticCode=int(tmp)
    ################################################
    nbgene=len(getGenes(txt))
    general={
        'description':description,
        'type':typeda,
        'data':data,
        'ID':ID,
        'length':leng,
        'gbtype':gbtype,
        'organism':organism,
        'number of gene':nbgene,
        'genes':getGenes(txt)
        }
    print ('========== General Information  ==========')
    print ('Description :',general['description'])
    print ('Type :',general['type'])
    print ('Data :',general['data'])
    print ('ID :',general['ID'])
    print ('Length :',general['length'])
    print ('GBtype :',general['gbtype'])
    print ('Organism :',general['organism'])
    print ('Number of gene :',general['number of gene'])
    print ('=========  GENES  =========')
    for i in general['genes']:
        print ('Start :',i['start'])
        print ('Stop :',i['stop'])
        print ('Length :',i['length'])
        print ('Frame:',i['frame'])
        print ('Name :',i['name'])
        print ('Protein :',i['protein'])
        print ('Product :',i['product'])
        print ('======================')
    return general

def read_fasta(filename):
    file=codecs.open(filename,"r",encoding="utf-8")
    seq=''
    for line in file.readlines():
        if not line:
            break
        if line.startswith(">"):
            pass
        else:
            seq=seq+line
    return seq

def menu():
    print "======================================== MENU ========================================="
    print "\n"
    print "taper [1] chercher les ORFs d'une séquence"
    print "taper [2] afficher les ORFs"
    print "taper [0] pour quitter"
    print "\n"
    print "======================================================================================="

def threshold():
  print "[1] No threshold"
  print "[2] 90pb"
  print "[3] 210pb"
  print "[4] 300pb"
  print "[5] 420pb"
  threshold = raw_input()
  if threshold == "1":
    threshold = 1
  elif threshold == "2":
    threshold = 90
  elif threshold == "3":
    threshold = 210
  elif threshold == "4":
    threshold = 300
  elif threshold == "5":
    threshold= 420
  else :
    print "Erreur"
  return threshold

def commandes():
    nb=1
    while nb != 0 :
        menu()
        nb=raw_input()
        if nb == "1":
            fasta = raw_input("Entrer le nom de votre fichier FASTA")
            seq=read_fasta(fasta)
            id = input("Choisir l'ID")
            threshold = threshold() #possibilité de laisser l'utilisateur choisir avec un input
            findORF(seq, threshold, id)
        if nb == "2" :
            print fasta
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"
###MAIN####

commandes()
