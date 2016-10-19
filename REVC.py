string = open('rosalind_ba1c.txt').read().upper()
string = string[::-1].replace('C','g').replace('G','c').replace('T','a').replace('A','t').upper()
print string
