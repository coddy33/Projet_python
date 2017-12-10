#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Projet de programmation BioPython - Alone in the Dark
# BLASQUIZ Julie
# JUNG Frédéric
# THOUVENIN Arthur

import myBio as bio
import codecs
import os
import sys
import re

def geneticode():
    '''This function provide genetic codes to all function.

    Description:
        This function have 31 different genetic code (with some exceptions), there is only AAs and Starts variables that change through genetic codes
        and then we make all codes in a list containing codecs.

    Args:
        No Args needed

    Return:
        listcode: a list containing different genetic codes.
    '''
    listcode=['nothing']
    Base1 ='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
    Base2 ='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
    Base3 ='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
    #############################standard code 1
    AAs   ='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts='---M------**--*----M---------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    #############################The Vertebrate Mitochondrial Code 2
    AAs   ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG'
    Starts='----------**--------------------MMMM----------**---M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ##############################The Yeast Mitochondrial Code 3
    AAs   ='FFLLSSSSYY**CCWWTTTTPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts='----------**----------------------MM----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ The Mold, Protozoan, and Coelenterate Mitochondrial Code and the Mycoplasma/Spiroplasma Code (transl_table=4)
    AAs   ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts='--MM------**-------M------------MMMM---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ The Invertebrate Mitochondrial Code (transl_table=5)
    AAs   ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSSSVVVVAAAADDEEGGGG'
    Starts='---M------**--------------------MMMM---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ The Ciliate, Dasycladacean and Hexamita Nuclear Code (transl_table=6)
    AAs    ='FFLLSSSSYYQQCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='--------------*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Code 7 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################ Code 8 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################ The Echinoderm and Flatworm Mitochondrial Code (transl_table=9)
    AAs    ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG'
    Starts ='----------**-----------------------M---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ The Euplotid Nuclear Code (transl_table=10)
    AAs    ='FFLLSSSSYY**CCCWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='----------**-----------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################# The Bacterial, Archaeal and Plant Plastid Code (transl_table=11)
    AAs    ='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='---M------**--*----M------------MMMM---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################  The Alternative Yeast Nuclear Code (transl_table=12)
    AAs    ='FFLLSSSSYY**CC*WLLLSPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='----------**--*----M---------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ The Ascidian Mitochondrial Code (transl_table=13)
    AAs    ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSGGVVVVAAAADDEEGGGG'
    Starts ='---M------**----------------------MM---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################# The Alternative Flatworm Mitochondrial Code (transl_table=14)
    AAs    ='FFLLSSSSYYY*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG'
    Starts ='-----------*-----------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################# Code 15 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################# Chlorophycean Mitochondrial Code (transl_table=16)
    AAs    ='FFLLSSSSYY*LCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='----------*---*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################# Code 17 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################# Code 18 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################# Code 19 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################# Code 20 NO AVAILABLE ON NCBI
    listcode.append(listcode[1])
    ################################# Trematode Mitochondrial Code (transl_table=21)
    AAs    ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNNKSSSSVVVVAAAADDEEGGGG'
    Starts ='----------**-----------------------M---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Scenedesmus obliquus Mitochondrial Code (transl_table=22)
    AAs    ='FFLLSS*SYY*LCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='------*---*---*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Thraustochytrium Mitochondrial Code (transl_table=23)
    AAs    ='FF*LSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='--*-------**--*-----------------M--M---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Pterobranchia Mitochondrial Code (transl_table=24)
    AAs    ='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSSKVVVVAAAADDEEGGGG'
    Starts ='---M------**-------M---------------M---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ############################### Candidate Division SR1 and Gracilibacteria Code (transl_table=25)
    AAs    ='FFLLSSSSYY**CCGWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='---M------**-----------------------M---------------M------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Pachysolen tannophilus Nuclear Code (transl_table=26)
    AAs    ='FFLLSSSSYY**CC*WLLLAPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='----------**--*----M---------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Karyorelict Nuclear (transl_table=27)
    AAs    ='FFLLSSSSYYQQCCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='--------------*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Condylostoma Nuclear (transl_table=28)
    AAs    ='FFLLSSSSYYQQCCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='----------**--*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Mesodinium Nuclear (transl_table=29)
    AAs    ='FFLLSSSSYYYYCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='--------------*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Peritrich Nuclear (transl_table=30)
    AAs    ='FFLLSSSSYYEECC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='--------------*--------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ################################ Blastocrithidia Nuclear (transl_table=31)
    AAs    ='FFLLSSSSYYEECCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
    Starts ='----------**-----------------------M----------------------------'
    list1=[AAs,Starts,Base1,Base2,Base3]
    listcode.append(list1)
    ###########################################################################
    return listcode

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

def getGeneticCode(num):
    '''This function get genetic code specify by user.

    Description:
        In this function we take genetic codes from function geneticode() and then we choose in the list the code choose by user. Then we return a dictionnary from the specify genetic code.

    Args:
        num: NCBI_ID corresponding to one of 31 different genetic codes

    Return:
        dicocode: a dictionnary of codon corresponding to an AA.

    '''
    listcode=geneticode()
    dicocode={}
    nb=int(num)
    for i in range(len(listcode[nb][0])):
        codon=listcode[nb][2][i]+listcode[nb][3][i]+listcode[nb][4][i]
        dicocode.update({codon:listcode[nb][0][i]})
    return dicocode

def getGeneticCodeStart(num):
    '''This function get genetic code specify by userand return Start codons.

    Description:
        In this function we take genetic codes from function geneticode() and then we choose in the list the code choose by user. Then we return a dictionnary from the specify genetic code of all start codons.

    Args:
        num: NCBI_ID corresponding to one of 31 different genetic codes

    Return:
        dicocode: a dictionnary of codon start corresponding to an AA.
    '''
    dicocodestart={}
    listcode=geneticode()
    nb=int(num)
    for i in range(len(listcode[nb][1])):
        if listcode[nb][1][i]!='-' and listcode[nb][1][i]!='*':
            codon=listcode[nb][2][i]+listcode[nb][3][i]+listcode[nb][4][i]
            dicocodestart.update({codon:listcode[nb][1][i]})
    return dicocodestart

def getGeneticCodeStop(num):
    '''This function get genetic code specify by userand return Stop codons.

    Description:
        In this function we take genetic codes from function geneticode() and then we choose in the list the code choose by user. Then we return a dictionnary from the specify genetic code of all stop codons.

    Args:
        num: NCBI_ID corresponding to one of 31 different genetic codes

    Return:
        dicocode: a dictionnary of codon stop corresponding to an AA.
    '''
    dicocodestop={}
    listcode=geneticode()
    nb=int(num)
    for i in range(len(listcode[nb][1])):
        if listcode[nb][1][i]!='-' and listcode[nb][1][i]!='M':
            codon=listcode[nb][2][i]+listcode[nb][3][i]+listcode[nb][4][i]
            dicocodestop.update({codon:listcode[nb][1][i]})
    return dicocodestop

def findORF(seq, threshold,id,sens):
    '''This function is the main function of our script this function call all other to make the programm work

    Description:
        In this function we go through sequence, given by user, and all frames to get orfs from sequence.
        Then we return those in a list of dictionnary, each dictionary contain information about the orf detected.

    Args:
        seq: a nucleic sequence
        treshold: the minimumof ORF length in bp
        id: NCBI_ID of genetic code table
        sens: sens of the analyse (1 or -1)

    Return:
        ORF_csv: A list containning dictionaries of orf and it's information.
    '''
    ORF_csv=[]
    start_dico=getGeneticCodeStart(id)
    start=start_dico.keys()
    stop_dico=getGeneticCodeStop(id)
    stop=stop_dico.keys()
    for i in [0,1,2]:
        j=i
        while i <= len(seq):
                if bio.isCodonStart(seq,i,start_dico) == True:
                    for k in range(i,len(seq),3):
                        if bio.isCodonStop(seq,k,stop) == True :
                            lenORF=k-i
                            if lenORF >= threshold:
                                seq_nuc = seq[i:k+3]
                                seq_nuc = seq_nuc.encode('ascii')
                                seq_aa=translate(seq_nuc,id)
                                D={"start":i,
                                       "stop":k,
                                       "length":lenORF,
                                       "frame":sens*(j+1), ### -1 pour antisens
                                       "sequencean1":seq_nuc,
                                       "sequenceaa":seq_aa}
                                ORF_csv.append(D)
                            i=k
                            break
                i=i+3

    return ORF_csv

def translate(orf,id):
    ''' This function allow to translate nucleic sequence into acide amine sequence

    Description:
        This function translate nucleic sequence to proteic sequence through dictionnary get by getGeneticCode(num)

    Args :
        orf: the ORF to translate
        id: the code Table id

    Return:
        seqprot: The sequence that have been translate.
    '''
    seqprot=''
    dico=getGeneticCode(id)
    j=0
    while j<len(orf):
        try:
            seqprot=seqprot+dico[bio.oneWord(orf,j,3)]
        except KeyError:
            seqprot=seqprot+'X'
        j=j+3

    return seqprot

def getLengths(listdic):
    '''This function determine the length of ORFs

    Description:
        This function use the list of ORFs and use length of each element to know lengths

    Args:
        listdic: list of dictionnary containing ORF informations produce by findORF(seq,threshold,id,sens) function

    Return:
        sizelistbp: First list where sizes are in bp
        sizelistaa: Second list where sizes are in aa
    '''
    sizelistbp=[]
    sizelistaa=[]
    for i in listdic:
        size=i['length']
        size = int(size)
        sizelistbp.append(size)
        sizeaa=size/3
        sizelistaa.append(sizeaa)
    return sizelistbp,sizelistaa

def getLongestORF(ORF):
    '''This function get the longest ORF of all ORF detected by program

    Description:
        This function get lengths of all ORF through getLengths(ORF), and then return the indice of the longest ORF to find the longest ORF of the list containg all dictionaries

    Args:
        ORF: global variable, a list of dictionaries containing all information about ORFs

    Return:
        ORF[indice]: a dictionnary of the longest ORF detected
    '''
    result=getLengths(ORF)
    result=result[0]
    x=0
    for i in result:
        if i>x:
            x=i
    maxi=x
    indice=0
    for i in result:
        if i==maxi:
            return ORF[indice]
        else:
            indice=indice+1

def getTopLongestORF(ORF,value):
    '''This function get (value%) of longest ORF of all ORF detected by program

    Description:
        This function get lengths of all ORF through getLengths(ORF), and then use a temporary list to delete (value%) of longest ORF that is kept in another list.
        Then we return (value%) of longest ORF of all ORF detected by program through the list topvalues.

    Args:
        ORF: global variable, a list of dictionaries containing all information about ORFs
        value: a value of percent

    Return:
        topvalues: a list containing dictionnaries of (value%) of longest ORF of all ORF detected by program.
    '''
    topvalues=[]
    tmp=ORF
    s=len(tmp)
    s=value*s
    while s>0:
        y=getLongestORF(tmp)
        topvalues.append(y)
        tmp.pop(tmp.index(y))
        s=s-1
    return topvalues

def writeCSV(listdict,filename, sep):
    '''This function allow current programm to save in file which the name is choosen

    Description:
        In this function we open a file which name is choose by the user and then we write a list of dictionaries about ORFs

    Args:
        listdict: a list of dictionaries about ORFs
        filename: file name
        sep: separator for save objects in filename

    Return:
        Nothing to return.
    '''
    file=open(filename,"w")
    j=0
    file.write('>ORF')
    file.write(sep)
    file.write('Start')
    file.write(sep)
    file.write('Stop')
    file.write(sep)
    file.write('Length')
    file.write(sep)
    file.write('Frame')
    file.write(sep)
    file.write('Seq an')
    file.write(sep)
    file.write('Seq aa')
    file.write('\n')
    for i in listdict:##################  Pour un dico
        file.write('ORF'+str(j))#+(str(j)).encode('ascii'))###########################ajouter des chiffres qui s'additione pour ORF
        file.write(sep)
        file.write(str(i['start']))
        file.write(sep)
        file.write(str(i['stop']))
        file.write(sep)
        file.write(str(i['length']))
        file.write(sep)
        file.write(str(i['frame']))
        file.write(sep)
        file.write(i['sequencean1'])
        file.write(sep)
        file.write(i['sequenceaa'])
        file.write('\n')
        j=j+1

def readCSV(filename, sep):
    '''This function allow current programm to load a file

    Description:
        User choose file to load and then this functio open file and read line by line, first line = listkey, second line = listvalues
        Then we make a dictionnary from those lists, and at the end one big list containing all dictionaries.

    Args:
        filename: file name
        sep: separator for load objects in filename

    Return:
        listdictorf: A list of dictionaries about ORFs
    '''
    file=open(filename,"r")
    listdictorf=[]
    values=[]
    Dic={}
    for line in file.readlines():
        if not line:
            break
        if line.startswith('>'):
            pass
        if line.startswith('ORF'):
            value=line.split(sep)
            seqaa=value[6]
            seqaa=seqaa[:-1]
            Dic={"start":value[1],
                "stop":value[2],
                "length":value[3],
                "frame":value[4], ### -1 pour antisens
                "sequencean1":value[5],
                "sequenceaa":seqaa}
        listdictorf.append(Dic)
    del listdictorf[0]
    return listdictorf################revoir dict

def compare(orflist1,orflist2):###############same size?+revoir################################################################################
    '''This function compare two list of orf and returns orfs which are present in those two lists.
    Description:
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

    Description:
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

def readGenBank(filename):
    '''This function call other function to read the GenBank of a read FlatFile

    Description:
        In this function we call two function first one to read FlatFile given by user then second one to take and return all information about the FlatFile.

    Args:
        filename : The file Name

    Return:
        Nothing to return
    '''
    txt=readFlatFile(filename)
    register_general(txt)

def register_general(txt):
    '''This function take general information about FlatFile given by user.

    Description:
        In this function we find and take all information about sequence in the file.
        Then we return those information in a list of dictionaries of ORFs

    Args:
        txt: a string containing the FlatFile

    Return:
        general: a list of dictionaries of ORFs
    '''
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
    '''This function read a FASTA file and return the sequence in this fasta file.

    Description:
        In this function we open a file and read it to take the sequence which is in the file.

    Args:
        filename: The file name

    Return:
        seq: The sequence which is used to find ORFs
    '''
    file=codecs.open(filename,"r",encoding="utf-8")
    seq=''
    for line in file.readlines():
        if not line:
            break
        if line.startswith(">"):
            pass
        else:
            seq=seq+line[:len(line)-2]
    return seq

def menu():
    '''This function print a MENU

    Description:
        This function print a Menu to help user

    Args:
        No Args needed

    Return:
        No return needed
    '''
    print "======================================== MENU ========================================="
    print "\n"
    print "taper [1] Afficher le nombre d'ORF trouvé"#################################################################
    print "taper [2] Afficher l'ORF le plus grand"
    print "taper [3] Afficher les x %/ ORFs les plus grand"
    print "taper [4] Afficher les gènes et information d'un FlatFile de NCBI"
    print "taper [5] "
    print "taper [0] pour quitter"
    print "\n"
    print "======================================================================================="

def nb1menu():
    '''This function correspond to findORF() and a save of results

    Description:
        In this function we call many function to find orf in a fasta file, first we read the fasta given by user, then we use the function findORF() to find ORFs,
        Then we keep all results in a list of dictionaries call dico_ORF then we ask user if he want to save in a CSV file.
        At the end we return the list of dictionaries.

    Args:
        No Args needed

    Return:
        dico_ORF: a list of dictionaries
    '''
    fasta = raw_input("Entrer le nom de votre fichier FASTA\n")
    seq_sens=read_fasta(fasta)
    seq_antisens=bio.reverse(seq_sens)
    id=input("Choisir l'ID\n")
    threshold=input("Entrer le threshold :\n")
    dico_ORF_sens=findORF(seq_sens, threshold,id,1)
    dico_ORF_antisens=findORF(seq_antisens,threshold,id,-1)
    dico_ORF = dico_ORF_sens + dico_ORF_antisens
    print '''
    Voulez-vous sauvegarder au format .csv?
    [1] Oui
    [0] Non
    '''
    choice=raw_input()
    if choice=="1":
        filename=raw_input('Choisir le nom de votre fichier de sauvegarde : \n')
        sep=raw_input('Choisissez le nom du séparateur utilisé dans le fichier de sauvegarde : ";" ou "," ou ":"\n')
        writeCSV(dico_ORF,filename, sep)
    else:
        pass
    return dico_ORF

def commandes(ORF):
    '''This function is the skeleton of our program, it call all other function to make program work well.

    Description:
        This function is a menu that call function in agreement with user choice.

    Args:
        ORF: list of dictionaries of ORFs information.

    Return:
        Nothing to return.
    '''
    nb=1
    os.system("clear")
    while nb != 0 :
        menu()
        nb=raw_input()
        if nb == "1":
            print len(ORF), "trouvés"
        elif nb == "2" :
            doc=getLongestORF(ORF)
            print '======  ORF  ====='
            print 'Start :',doc['start']
            print 'Stop :',doc['stop']
            print 'Length :',doc['length']
            print 'Frame:',doc['frame']
            print 'Nucleic sequence :',doc['sequencean1']
            print 'AAs sequence :',doc['sequenceaa']
            print '\n'
        elif nb == "3":
            print 'Entrer le pourcentage souhaité de 0.0 à 1.0\n'
            num=input()
            num=float(num)
            if num<0:
                print "ERREUR : mauvaise valeur"
            elif num>1:
                print "ERREUR : mauvaise valeur"
            else:
                diqo=getTopLongestORF(ORF,num)
                for i in diqo:
                    print '======  ORF  ====='
                    print 'Start :',i['start']
                    print 'Stop :',i['stop']
                    print 'Length :',i['length']
                    print 'Frame:',i['frame']
                    print 'Nucleic sequence :',i['sequencean1']
                    print 'AAs sequence :',i['sequenceaa']
                    print '\n'
        elif nb == "4":
            print 'Entrer le nom du fichier contenant le FlatFile : '
            filename=raw_input()
            readGenBank(filename)
        elif nb == "5":
            pass###############################################################    mise en page
        elif nb == "0":
            print "Bye"
            sys.exit()
        else:
            print "ERREUR : mauvaise valeur"

def start():
    '''This function corresponds to the initialization of our program

    Description:
        In this function we ask user if he want to start from a save file or a fasta file to analyse orf in the sequence

    Args:
        No Args needed

    Return:
        LISTDICO: A list of dictionaries of ORFs informations
    '''
    os.system("clear")
    print'''
       ____  ____  ______   _______           __                      ___    __                    _          __  __                __           __      ___    _____
      / __ \/ __ \/ ____/  / ____(_)___  ____/ /__  _____            /   |  / /___  ____  ___     (_)___     / /_/ /_  ___     ____/ /___ ______/ /__   |__ \  / __  /
     / / / / /_/ / /_     / /_  / / __ \/ __  / _ \/ ___/  ______   / /| | / / __ \/ __ \/ _ \   / / __ \   / __/ __ \/ _ \   / __  / __ `/ ___/ //_/   __/ / / / / /
    / /_/ / _, _/ __/    / __/ / / / / / /_/ /  __/ /     /_____/  / ___ |/ / /_/ / / / /  __/  / / / / /  / /_/ / / /  __/  / /_/ / /_/ / /  / ,<     / __/_/ /_/ /
    \____/_/ |_/_/      /_/   /_/_/ /_/\__,_/\___/_/              /_/  |_/_/\____/_/ /_/\___/  /_/_/ /_/   \__/_/ /_/\___/   \__,_/\__,_/_/  /_/|_|   /____(_)____/
    '''
    print'''
    Bienvenue sur ORFinder,

    [1] Voulez vous commencer à partir d'un fichier de sauvegarde d'une analyse précédente.

    [2] Voulez vous rechercher les ORFs d'une séquence donnée.

    [0] Quitter.
    '''
    LISTDICO=[]
    choice=raw_input()
    if choice=="0":
        sys.exit()
    elif choice=="1":
        filename=raw_input('Choisir le nom de votre fichier de sauvegarde : \n')
        sep=raw_input('Choisissez le nom du séparateur utilisé dans le fichier de sauvegarde : ";" ou "," ou ":"\n')
        LISTDICO=readCSV(filename,sep)
        #print LISTDICO
    elif choice=="2":
        LISTDICO=nb1menu()
        #print LISTDICO
    else:
        print "ERREUR : mauvaise valeur"
    return LISTDICO

###MAIN####
ORF=start()
commandes(ORF)
