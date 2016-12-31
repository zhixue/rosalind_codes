for line in open('rosalind_test.txt'):
    st = line.rstrip()
#acgt=8,4,2,1
print(st.count('A')*8+st.count('C')*4+st.count('G')*2+st.count('T'))