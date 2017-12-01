"""
Projet BioPython

"""

import myBio as bio
import myProject as proj

"""
try:
    NCBI_ID = raw_input("ID :")
"""

standard = bio.getStandardCode()
myTable  = proj.getGeneticCode(1) # Standard genetic code table

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

def getGeneticCode(NCBI_ID):
    '''This function is used to get genetic code from NCBI with an ID (1 to 31).

    Description:
        This function make 3 objects:
            - 1 dictionnary
            - 2 list
        First, dictionnary(dicocode_1) is the storage for genetic code and with ID we modify it to correspond to the correct genetic code.
        Sometimes we need to ask USER what is the specie which is analyse.
        Then a list of initiating codon(codon_initiateur), where we store each specific start codon.
        And at the end a list of stop codon(codon_stop), where we store each specific stop codon.

    Args:
        NCBI_ID: an identifier ofgenetic code.

    Return:
        dicocode_1: dictionnary containing the genetic code corresponding to the ID.
        codon_initiateur: list of initiating codon specific of the ID.
        codon_stop: list of stopping codon specific of the ID.
    '''
    codon_initiateur = ["ATG",]
    codon_stop = ["TAG"],["TAA"],["TGA"]

    dicocode_1 = {
    ["TTT"]:"Phe",["TTC"]:"Phe",["TTA"]:"Leu",["TTG"]:"Leu",
    ["CTT"]:"Leu",["CTC"]:"Leu",["CTA"]:"Leu",["CTG"]:"Leu",
    ["ATT"]:"Ile",["ATC"]:"Ile",["ATA"]:"Ile",["ATG"]:"Met",
    ["GTT"]:"Val",["GTC"]:"Val",["GTA"]:"Val",["GTG"]:"Val",
    ["TCT"]:"Ser",["TCC"]:"Ser",["TCA"]:"Ser",["TCG"]:"Ser",
    ["CCT"]:"Pro",["CCC"]:"Pro",["CCA"]:"Pro",["CCG"]:"Pro",
    ["ACT"]:"Thr",["ACC"]:"Thr",["ACA"]:"Thr",["ACG"]:"Thr",
    ["GCT"]:"Ala",["GCC"]:"Ala",["GCA"]:"Ala",["GCG"]:"Ala",
    ["GGG"]:"Gly",["GGA"]:"Gly",["GGC"]:"Gly",["GGT"]:"Gly",
    ["AGG"]:"Arg",["AGA"]:"Arg",["AGC"]:"Ser",["AGT"]:"AGT",
    ["CGG"]:"Arg",["CGA"]:"Arg",["CGC"]:"Arg",["CGT"]:"Arg",
    ["TGG"]:"Trp",["TGA"]:"STOP",["TGC"]:"Cys",["TGT"]:"Cys",#1stop
    ["GAG"]:"Glu",["GAA"]:"Glu",["GAC"]:"Asp",["GAT"]:"Asp",
    ["AAG"]:"Lys",["AAA"]:"Lys",["AAC"]:"Asn",["AAT"]:"Asn",
    ["CAG"]:"Gln",["CAA"]:"Gln",["CAC"]:"His",["CAT"]:"His",
    ["TAG"]:"STOP",["TAA"]:"STOP",["TAC"]:"Tyr",["TAT"]:"Tyr"}#2stop
    if NCBI_ID==1:############################################################
        continue
    if NCBI_ID==2:############################################################
        ###########DICO#########
        dicocode_1["AGA"]="Ter"
        dicocode_1["AGG"]:"Ter"
        dicocode_1["ATA"]:"Met"
        dicocode_1["TGA"]:"Trp"
        ########STOP############
        codon_stop.pop(2)
        ########INIT############
        print '''
            [1] Bos
            [2] Homo
            [3] Mus
            [4] Coturnix, Gallus
            '''
        sp=input('Which specie do you want?')
        if sp==1:
            codon_initiateur.append("ATA")
        if sp==2:
            codon_initiateur.append("ATA")
            codon_initiateur.append("ATT")
        if sp==3:
            codon_initiateur.append("ATA")
            codon_initiateur.append("ATT")
            codon_initiateur.append("ATC")
        if sp==4:
            codon_initiateur.append("GTG")
    if NCBI_ID==3:############################################################
        ###########DICO#########
        dicocode_1["ATA"]:"Met"
        dicocode_1["CTT"]:"Thr"
        dicocode_1["CTC"]:"Thr"
        dicocode_1["CTA"]:"Thr"
        dicocode_1["CTG"]:"Thr"
        dicocode_1["TGA"]:"Trp"
        del dicocode_1["CGA"]
        del dicocode_1["CGC"]
        ###########STOP#########
        codon_stop.pop(2)
    if NCBI_ID==4:############################################################
        ###########DICO#########
        dicocode_1["UGA"]:"Trp"
        ########INIT############
        print '''
            [1] Trypanosoma
            [2] Leishmania
            [3] Tetrahymena
            [4] Paramecium
            '''
        sp=input('Which specie do you want?')
        if sp==1:
            codon_initiateur.append("TTA")
            codon_initiateur.append("TTG")
            codon_initiateur.append("CTG")
        if sp==2:
            codon_initiateur.append("ATT")
            codon_initiateur.append("ATA")
        if sp==3:
            codon_initiateur.append("ATT")
            codon_initiateur.append("ATA")
            codon_initiateur.append("ATG")
        if sp==4:
            codon_initiateur.append("ATT")
            codon_initiateur.append("ATA")
            codon_initiateur.append("ATG")
            codon_initiateur.append("ATC")
            codon_initiateur.append("GTG")
            codon_initiateur.append("GTA")
    if NCBI_ID==5:############################################################
        ###########DICO#########
        dicocode_1["AGA"]:"Ser"
        dicocode_1["AGG"]:"Ser"
        dicocode_1["ATA"]:"Met"
        dicocode_1["TGA"]:"Trp"
        print '''
            [1] Yes
            [0] No
            '''
        droso=input('Is it Drosophila')
        if droso==1:
            del dicocode_1["AGG"]
        if droso==0:
            continue
        ###########STOP#########
        codon_stop.pop(2)
        ########INIT############
        print '''
            [1] Apis
            [2] Polyplacophora
            [3] Ascaris, Caernorhabditis
            '''
        sp=input('Which specie do you want?')
        codon_initiateur.append("ATA")
        codon_initiateur.append("ATT")
            if sp==1:
            codon_initiateur.append("ATC")
            if sp==2:
            codon_initiateur.append("GTG")
            if sp==3:
            codon_initiateur.append("TTG")
    if NCBI_ID==6:############################################################
        ###########DICO#########
        dicocode_1["TAA"]:"Gln"
        dicocode_1["TAG"]:"Gln"
        ########STOP############
        codon_stop.pop(0)
        codon_stop.pop(1)
    if NCBI_ID==9:############################################################
        ###########DICO#########
        dicocode_1["AAA"]:"Asn"
        dicocode_1["AGA"]:"Ser"
        dicocode_1["AGG"]:"Ser"
        dicocode_1["TGA"]:"Trp"
        ########STOP############
        codon_stop.pop(2)
    if NCBI_ID==10:###########################################################
        ###########DICO#########
        dicocode_1["TGA"]:"Cys"
        ########STOP############
        codon_stop.pop(2)
    if NCBI_ID==11:###########################################################
        continue
    if NCBI_ID==12:###########################################################
        ###########DICO#########
        dicocode_1["CTG"]:"Ser"
        ########INIT############
        codon_initiateur.append("CAG")
    if NCBI_ID==13:###########################################################
        ###########DICO#########
        dicocode_1["AGA"]:"Gly"
        dicocode_1["AGG"]:"Gly"
        dicocode_1["ATA"]:"Met"
        dicocode_1["TGA"]:"Trp"
        ########STOP############
        codon_stop.pop(2)
        ########INIT############
        codon_initiateur.append("ATA")
        codon_initiateur.append("GTG")
        codon_initiateur.append("TTG")
        codon_initiateur.append("ATA")
    if NCBI_ID==14:###########################################################
        ###########DICO#########
        dicocode_1["AAA"]:"Asn"
        dicocode_1["AGA"]:"Ser"
        dicocode_1["AGG"]:"Ser"
        dicocode_1["TAA"]:"Tyr"
        dicocode_1["TGA"]:"Trp"
        ########STOP############
        codon_stop.pop(1)
        codon_stop.pop(2)
    if NCBI_ID==16:###########################################################
        ###########DICO#########
        dicocode_1["TAG"]:"Leu"
        ########STOP############
        codon_stop.pop(0)
    if NCBI_ID==21:###########################################################
        ###########DICO#########
        dicocode_1["TGA"]:"Trp"
        dicocode_1["ATA"]:"Met"
        dicocode_1["AGA"]:"Ser"
        dicocode_1["AGG"]:"Ser"
        dicocode_1["AAA"]:"Asn"
        ########STOP############
        codon_stop.pop(2)
    if NCBI_ID==22:###########################################################
        ###########DICO#########
        dicocode_1["TCA"]:"STOP"
        dicocode_1["TAG"]:"Leu"
        ########STOP############
        codon_stop.pop(0)
    if NCBI_ID==23:###########################################################
        continue
    if NCBI_ID==24:###########################################################
        ###########DICO#########
        dicocode_1["AGA"]:"Ser"
        dicocode_1["AGG"]:"Lys"
        dicocode_1["TGA"]:"Trp"
        ########STOP############
        codon_stop.pop(2)
    if NCBI_ID==25:###########################################################
        ###########DICO#########
        dicocode_1["TGA"]:"Gly"
        ########INIT############
        codon_initiateur = ["AUG","GUG","UUG"]
        ########STOP############
        codon_stop.pop(2)
    if NCBI_ID==26:###########################################################
        ###########DICO#########
        dicocode_1["CTG"]:"Ala"
        ########INIT############
        codon_initiateur = ["AUG","GUG","UUG"]
    if NCBI_ID==27:###########################################################
        ###########DICO#########
        dicocode_1["TAG"]:"Gln"
        dicocode_1["TAA"]:"Gln"
        dicocode_1["TGA"]:"STOP"
        ########STOP############
        codon_stop.pop(1)
        codon_stop.pop(0)
    if NCBI_ID==28:###########################################################
        ###########DICO#########
        dicocode_1["TGA"]:"STOP"
        dicocode_1["TAG"]:"STOP"
        dicocode_1["UAA"]:"STOP"
    if NCBI_ID==29:###########################################################
        ###########DICO#########
        dicocode_1["TAA"]:"Tyr"
        dicocode_1["TAG"]:"Tyr"
        ########INIT############
        codon_initiateur = ["ATG"]
        ########STOP############
        codon_stop.pop(1)
        codon_stop.pop(0)
    if NCBI_ID==30:###########################################################
        ###########DICO#########
        dicocode_1["TAA"]:"Glu"
        dicocode_1["TAG"]:"Glu"
        ########STOP############
        codon_stop.pop(1)
        codon_stop.pop(0)
    if NCBI_ID==31:###########################################################
        ###########DICO#########
        dicocode_1["TGA"]:"Trp"
        dicocode_1["TAG"]:"STOP"
        dicocode_1["TAA"]:"STOP"
        ########STOP############
        codon_stop.pop(2)
    return dicocode_1,codon_stop,codon_initiateur



#####################################################################################################################################################################################################################
def findORF(seq, treshold, codeTable):
    '''This function is the main function of our script this function call all other to make the programm work

    Description:

    Args:
        seq: a nucleic sequence
        treshold: the minimumof ORF length in bp
        codeTable: a genetic code table

    Return:
        list of ORFs

    '''
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

    for i in list_ORF:
        translate(i)




###########################################################"""

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



result = getGeneticCode(NCBI_ID)
result[0] #CodeTable
