def getGenes(txt):
    remove=txt.partition(' gene ')[0]
    txt=txt[len(remove):]
    tmp=txt###########remove before first gene
    length=tmp.count(' gene ')#number of gene?
    for i in range(length):#boucle number of gene
        remove=txt.partition(' gene  ')[2].partition(' gene ')[0]
        txt=txt[len(remove):]
        tmp=txt
        try:
            start=tmp.partition('gene         ')[2].partition('..')[0]
            start=int(start)
        except ValueError:
            start=tmp.partition('complement(')[2].partition('..')[0]
            start=int(start)
        try:
            stop=tmp.partition('..')[2].partition('\n')[0]
            stop=int(stop)
        except ValueError:
            stop=tmp.partition('..')[2].partition(')\n')[0]
            stop=int(stop)
        length=stop-start
        name=''
        name=tmp.partition('gene=\"')[2].partition('\"')[0]
        if name == '':
            name='unknow'
        protein=''
        protein=tmp.partition('/protein_id=\"')[2].partition('\"')[0]
        if protein=='':
            protein='xxx'
        product=''
        product=tmp.partition('/product=\"')[2].partition('\"')[0]
        if product=='':
            product='unknown'
        remove=txt.partition(' gene ')[0]
        txt=txt[len(remove):]
        tmp=txt
        #print (tmp)
        print (start)
        print (stop)
        print (length)
        print (name)
        print (protein)
        print (product)

Flat='''
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
     CDS             complement(join(8623..12026,12104..19613,19671..19982,
                     20050..20484))
                     /locus_tag="ANI_1_1496094"
                     /old_locus_tag="An11g00050"
                     /codon_start=1
                     /product="hypothetical protein"
                     /protein_id="XP_001394009.2"
                     /db_xref="GeneID:4984252"
    '''


getGenes(Flat)