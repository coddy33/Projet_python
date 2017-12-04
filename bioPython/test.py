def getGenes(txt):
    remove=txt.partition('gene  ')[0]
    txt=txt[len(remove):]
    tmp=txt##########################################################################################remove before first gene
    length=tmp.count(' gene  ')#number of gene?
    firstg=tmp.partition('     gene            ')[0]
    print (firstg,'premier')##########################premier gene
    for i in range(length):
        firstg=tmp.partition('     gene            ')[0]
        tmp=tmp[len(firstg):]
        secondg=tmp.partition('     gene            ')[2].partition(' gene     ')[0]
        tmp=tmp[len(secondg):]
        print ('secondgene',secondg)###############j ai tout les genes qui defilent sauf premier
    

    '''try:
        start=tmp.partition('         ')[2].partition('..')[0]
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
    '''

    '''
    #print (tmp)
    print (start)
    print (stop)
    print (length)
    print (name)
    print (protein)
    print (product)
    '''

Flat='''
FEATURES             Location/Qualifiers
     source          1..2721467
                     /organism="Aspergillus niger CBS 513.88"
                     /mol_type="genomic DNA"
                     /db_xref="taxon:425011"
     gene            complement(1391..4000)
                     TEST1111111111111"
     gene            7717..8497
                     TEST2222222
     gene            complement(8623..20484)
                     TEST333333
     gene            complement(1391..4000)
                     TESTAAAAAAA"
     gene            7717..8497
                     TESTBBBBBBBBBBBBB
    '''


getGenes(Flat)