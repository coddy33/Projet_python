import re


listcode=[]
AAs='FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts='---M------**--*----M---------------M----------------------------'
Base1='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
list1=[AAs,Starts,Base1,Base2,Base3]
listcode.append(list1)


AAs='FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG'
Starts='----------**--------------------MMMM----------**---M------------'
Base1='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
list1=[AAs,Starts,Base1,Base2,Base3]
listcode.append(list1)

AAs='FFLLSSSSYY**CCWWTTTTPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
Starts='----------**----------------------MM----------------------------'
Base1='TTTTTTTTTTTTTTTTCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG'
Base2='TTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGGTTTTCCCCAAAAGGGG'
Base3='TCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAGTCAG'
list1=[AAs,Starts,Base1,Base2,Base3]
listcode.append(list1)

def getGeneticCode(AAs,Base1,Base2,Base3):
    dicocode={}
    for i in range(len(AAs)):
        codon=Base1[i]+Base2[i]+Base3[i]
        dicocode.update({codon:AAs[i]})
    print(dicocode)
    return dicocode


def getGeneticCodeStart(Starts,Base1,Base2,Base3):
    dicocodestart={}
    for i in range(len(Starts)):
        if Starts[i]!='-' and Starts[i]!='*':
            codon=Base1[i]+Base2[i]+Base3[i]
            dicocodestart.update({codon:Starts[i]})
    print (dicocodestart)
    return dicocodestart

def getGeneticCodeStop(Starts,Base1,Base2,Base3):
    dicocodestop={}
    for i in range(len(Starts)):
        if Starts[i]!='-' and Starts[i]!='M':
            codon=Base1[i]+Base2[i]+Base3[i]
            dicocodestop.update({codon:Starts[i]}) 
    print(dicocodestop)
    return dicocodestop







getGeneticCodeStop(Starts,Base1,Base2,Base3)
getGeneticCodeStart(Starts,Base1,Base2,Base3)
getGeneticCode(AAs,Base1,Base2,Base3)






def getGenes(txt):
    listdico=[]
    remove=txt.partition('gene  ')[0]
    txt=txt[len(remove):]
    tmp=txt##########################################################################################remove before first gene
    length=tmp.count(' gene  ')#number of gene?
    firstg=tmp.partition('     gene            ')[0]
    listdico.append(register_gene(firstg))
    #print (firstg,'premier')##########################premier gene
    for i in range(length):
        firstg=tmp.partition('     gene            ')[0]
        tmp=tmp[len(firstg):]
        secondg=tmp.partition('     gene            ')[2].partition(' gene     ')[0]
        listdico.append(register_gene(secondg))
        tmp=tmp[len(secondg):]
        #print ('secondgene',secondg)###############j ai tout les genes qui defilent sauf premier
    return listdico
    

def register_gene(tmp):
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

def register_general(txt):#miss genetic code
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


Flat='''
LOCUS       NT_166526            2721467 bp    DNA     linear   CON 03-MAR-2011
DEFINITION  Aspergillus niger CBS 513.88 clone An11.
ACCESSION   NT_166526
VERSION     NT_166526.1
DBLINK      Project: 19263
            BioProject: PRJNA19263
KEYWORDS    RefSeq.
SOURCE      Aspergillus niger CBS 513.88
  ORGANISM  Aspergillus niger CBS 513.88
            Eukaryota; Fungi; Dikarya; Ascomycota; Pezizomycotina;
            Eurotiomycetes; Eurotiomycetidae; Eurotiales; Aspergillaceae;
            Aspergillus.
REFERENCE   1  (bases 1 to 2721467)
  AUTHORS   Pel,H.J., de Winde,J.H., Archer,D.B., Dyer,P.S., Hofmann,G.,
            Schaap,P.J., Turner,G., de Vries,R.P., Albang,R., Albermann,K.,
            Andersen,M.R., Bendtsen,J.D., Benen,J.A., van den Berg,M.,
            Breestraat,S., Caddick,M.X., Contreras,R., Cornell,M.,
            Coutinho,P.M., Danchin,E.G., Debets,A.J., Dekker,P., van
            Dijck,P.W., van Dijk,A., Dijkhuizen,L., Driessen,A.J., d'Enfert,C.,
            Geysens,S., Goosen,C., Groot,G.S., de Groot,P.W., Guillemette,T.,
            Henrissat,B., Herweijer,M., van den Hombergh,J.P., van den
            Hondel,C.A., van der Heijden,R.T., van der Kaaij,R.M., Klis,F.M.,
            Kools,H.J., Kubicek,C.P., van Kuyk,P.A., Lauber,J., Lu,X., van der
            Maarel,M.J., Meulenberg,R., Menke,H., Mortimer,M.A., Nielsen,J.,
            Oliver,S.G., Olsthoorn,M., Pal,K., van Peij,N.N., Ram,A.F.,
            Rinas,U., Roubos,J.A., Sagt,C.M., Schmoll,M., Sun,J., Ussery,D.,
            Varga,J., Vervecken,W., van de Vondervoort,P.J., Wedler,H.,
            Wosten,H.A., Zeng,A.P., van Ooyen,A.J., Visser,J. and Stam,H.
  TITLE     Genome sequencing and analysis of the versatile cell factory
            Aspergillus niger CBS 513.88
  JOURNAL   Nat. Biotechnol. 25 (2), 221-231 (2007)
   PUBMED   17259976
REFERENCE   2  (bases 1 to 2721467)
  CONSRTM   NCBI Genome Project
  TITLE     Direct Submission
  JOURNAL   Submitted (06-JAN-2011) National Center for Biotechnology
            Information, NIH, Bethesda, MD 20894, USA
REFERENCE   3  (bases 1 to 2721467)
  AUTHORS   Pel,H.J.
  TITLE     Direct Submission
  JOURNAL   Submitted (01-MAY-2006) Pel H.J., DSM, 624-0295, P.O. Box 1, 2600
            MA Delft, THE NETHERLANDS
COMMENT     PROVISIONAL REFSEQ: This record has not yet been subject to final
            NCBI review. The reference sequence is identical to AM270990.
FEATURES             Location/Qualifiers
     source          1..2721467
                     /organism="Aspergillus niger CBS 513.88"
                     /mol_type="genomic DNA"
                     /db_xref="taxon:425011"
     gene            complement(1391..4000)
                     /locus_tag="ANI_1_1494094"
                     /old_locus_tag="An11g00010"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984233"
     mRNA            complement(join(1391..1560,1606..2041,2111..4000))
                     /locus_tag="ANI_1_1494094"
                     /old_locus_tag="An11g00010"
                     /product="dynamin family protein"
                     /transcript_id="XM_001393968.2"
                     /db_xref="GeneID:4984233"
     CDS             complement(join(1391..1560,1606..2041,2111..4000))
                     /locus_tag="ANI_1_1494094"
                     /old_locus_tag="An11g00010"
                     /codon_start=1
                     /product="dynamin family protein"
                     /protein_id="XP_001394005.2"
                     /db_xref="GeneID:4984233"
     gene            7717..8497
                     /locus_tag="ANI_1_2094"
                     /old_locus_tag="An11g00040"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984231"
     mRNA            join(7717..8061,8122..8497)
                     /locus_tag="ANI_1_2094"
                     /old_locus_tag="An11g00040"
                     /product="hypothetical protein"
                     /transcript_id="XM_001393971.2"
                     /db_xref="GeneID:4984231"
     CDS             join(7827..8061,8122..8231)
                     /locus_tag="ANI_1_2094"
                     /old_locus_tag="An11g00040"
                     /codon_start=1
                     /product="hypothetical protein"
                     /protein_id="XP_001394008.1"
                     /db_xref="GeneID:4984231"
     gene            complement(8623..20484)
                     /locus_tag="ANI_1_1496094"
                     /old_locus_tag="An11g00050"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984252"
     mRNA            complement(join(8623..12026,12104..19613,19671..19982,
                     20050..20484))
                     /locus_tag="ANI_1_1496094"
                     /old_locus_tag="An11g00050"
                     /product="hypothetical protein"
                     /transcript_id="XM_001393972.2"
                     /db_xref="GeneID:4984252"
     CDS             complement(join(8623..12026,12104..19613,19671..19982,
                     20050..20484))
                     /locus_tag="ANI_1_1496094"
                     /old_locus_tag="An11g00050"
                     /codon_start=1
                     /product="hypothetical protein"
                     /protein_id="XP_001394009.2"
                     /db_xref="GeneID:4984252"
     gene            complement(22153..23807)
                     /locus_tag="ANI_1_6094"
                     /old_locus_tag="An11g00060"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984258"
     mRNA            complement(join(22153..22709,22767..22862,22927..23306,
                     23363..23430,23486..23542,23597..23807))
                     /locus_tag="ANI_1_6094"
                     /old_locus_tag="An11g00060"
                     /product="integral membrane protein (Pth11)"
                     /transcript_id="XM_001393973.2"
                     /db_xref="GeneID:4984258"
     CDS             complement(join(22376..22709,22767..22862,22927..23306,
                     23363..23430,23486..23542,23597..23792))
                     /locus_tag="ANI_1_6094"
                     /old_locus_tag="An11g00060"
                     /codon_start=1
                     /product="integral membrane protein (Pth11)"
                     /protein_id="XP_001394010.1"
                     /db_xref="GeneID:4984258"
     gene            24879..26494
                     /locus_tag="ANI_1_8094"
                     /old_locus_tag="An11g00070"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984246"
     mRNA            join(24879..25083,25170..25296,25384..25507,25580..26031,
                     26104..26494)
                     /locus_tag="ANI_1_8094"
                     /old_locus_tag="An11g00070"
                     /product="O-methyltransferase"
                     /transcript_id="XM_001393974.2"
                     /db_xref="GeneID:4984246"
     CDS             join(24889..25083,25170..25296,25384..25507,25580..26031,
                     26104..26414)
                     /locus_tag="ANI_1_8094"
                     /old_locus_tag="An11g00070"
                     /codon_start=1
                     /product="O-methyltransferase"
                     /protein_id="XP_001394011.2"
                     /db_xref="GeneID:4984246"
     gene            complement(26946..28385)
                     /locus_tag="ANI_1_1498094"
                     /old_locus_tag="An11g00080"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984248"
     mRNA            complement(join(26946..27322,27470..27534,27589..27971,
                     28027..28134,28236..28385))
                     /locus_tag="ANI_1_1498094"
                     /old_locus_tag="An11g00080"
                     /product="P-type ATPase"
                     /transcript_id="XM_001393975.2"
                     /db_xref="GeneID:4984248"
     CDS             complement(join(26946..27322,27470..27534,27589..27971,
                     28027..28134,28236..28385))
                     /locus_tag="ANI_1_1498094"
                     /old_locus_tag="An11g00080"
                     /codon_start=1
                     /product="P-type ATPase"
                     /protein_id="XP_001394012.2"
                     /db_xref="GeneID:4984248"
     gene            complement(34405..35882)
                     /locus_tag="ANI_1_1500094"
                     /old_locus_tag="An11g00090"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984256"
     mRNA            complement(join(34405..34781,34841..34948,35000..35023,
                     35081..35131,35188..35407,35488..35540,35610..35775,
                     35856..35882))
                     /locus_tag="ANI_1_1500094"
                     /old_locus_tag="An11g00090"
                     /product="hypothetical protein"
                     /transcript_id="XM_001393976.2"
                     /db_xref="GeneID:4984256"
     CDS             complement(join(34405..34781,34841..34948,35000..35023,
                     35081..35131,35188..35407,35488..35540,35610..35775,
                     35856..35882))
                     /locus_tag="ANI_1_1500094"
                     /old_locus_tag="An11g00090"
                     /codon_start=1
                     /product="hypothetical protein"
                     /protein_id="XP_001394013.2"
                     /db_xref="GeneID:4984256"
     gene            complement(36800..38460)
                     /locus_tag="ANI_1_1502094"
                     /old_locus_tag="An11g00100"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984228"
     mRNA            complement(join(36800..37824,37881..38460))
                     /locus_tag="ANI_1_1502094"
                     /old_locus_tag="An11g00100"
                     /product="carboxylesterase"
                     /transcript_id="XM_001393977.2"
                     /db_xref="GeneID:4984228"
     CDS             complement(join(36800..37824,37881..38460))
                     /locus_tag="ANI_1_1502094"
                     /old_locus_tag="An11g00100"
                     /codon_start=1
                     /product="carboxylesterase"
                     /protein_id="XP_001394014.2"
                     /db_xref="GeneID:4984228"
     gene            complement(41114..42096)
                     /locus_tag="ANI_1_1504094"
                     /old_locus_tag="An11g00110"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984242"
     mRNA            complement(join(41114..41552,41612..41826,41886..41971,
                     42021..42096))
                     /locus_tag="ANI_1_1504094"
                     /old_locus_tag="An11g00110"
                     /product="cutinase 2"
                     /transcript_id="XM_001393978.1"
                     /db_xref="GeneID:4984242"
     CDS             complement(join(41114..41552,41612..41826,41886..41971,
                     42021..42096))
                     /locus_tag="ANI_1_1504094"
                     /old_locus_tag="An11g00110"
                     /codon_start=1
                     /product="cutinase 2"
                     /protein_id="XP_001394015.1"
                     /db_xref="GeneID:4984242"
     gene            complement(43347..45198)
                     /locus_tag="ANI_1_1506094"
                     /old_locus_tag="An11g00120"
                     /note="'Derived by automated computational analysis using
                     gene prediction method: Multi-Genome Gnomon'"
                     /db_xref="GeneID:4984264"
     mRNA            complement(join(43347..43429,43497..44102,44166..44621,
                     44702..44971,45081..45198))
                     /locus_tag="ANI_1_1506094"
                     /old_locus_tag="An11g00120"
                     /product="sugar transporter"
                     /transcript_id="XM_001393979.1"
                     /db_xref="GeneID:4984264"
     CDS             complement(join(43347..43429,43497..44102,44166..44621,
                     44702..44971,45081..45198))
                     /locus_tag="ANI_1_1506094"
                     /old_locus_tag="An11g00120"
                     /codon_start=1
                     /product="sugar transporter"
                     /protein_id="XP_001394016.1"
                     /db_xref="GeneID:4984264"
    '''


register_general(Flat)