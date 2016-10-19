import urllib2
import re
for one in open('rosalind_mprt.txt'):
    name = one.strip('\n')
    url = 'http://www.uniprot.org/uniprot/'+name+'.fasta'
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    start = the_page.find('\nM')
    seq = the_page[start+1:].replace('\n','')
    seq = ' '+seq
    regex = re.compile(r'N(?=[^P][ST][^P])')
    index = 0
    out = []
    '''

    out = [m.start() for m in re.finditer(regex, seq)]

    '''

    index = 0
    while(index<len(seq)):
        index += 1

        if re.search(regex,seq[index:]) == None:
            break


        #print S[index:]
        if re.match(regex,seq[index:]) != None:
            out.append(index)




    if out != []:
        print name
        print ' '.join([ str(i) for i in out])