S='CATCCCGCATCCCGCCCGTATCCCGCGATCCCGCATCCCGCATCCCGCCACTAATCCCGCGAATCCCGCTATCCCGCCCATCCCGCGCTATCCCGCATCCCGCCTAGGCTCGATCCCGCTAGTGAATCCCGCATCCCGCTAATCCCGCGATCCCGCATCCCGCTATCCCGCAATATCCCGCACTTAATCCCGCGTAAATCCCGCATCCCGCATCCCGCAGCCATCCCGCCGGATATGGTTATCATCCCGCCCCTAATCCCGCAAGTCCATCCCGCCATTATCCCGCCCGCGTTATCCCGCCTGATCTCTATCCCGCGCAATAGACTCGAAAATCCCGCTAGTCAACCCCATGAATCCCGCACCATCACGTTCTATCCCGCGATCTGCGGATCCCGCTCAAATCCCGCATCCCGCAGGTCAATCCCGCAATCCCGCATCCCGCCATTATCCCGCCAACGAAATCCCGCTCCCATCCCGCTGATCCCGCCGATCCCGCATCCCGCAATCCCGCCATCCCGCACATCCCGCATCCCGCGATCCCGCATCCCGCTGATCCCGCTAATCCCGCATCCCGCGTCATTCCATCCCGCCGGCATCCCGCCACTTGGTATCCCGCATCCCGCCACAGATCCCGCATCTTATCCCGCAAATCCCGCATCCCGCAATCCCGCCGCGAATCCCGCACTGTAACCGATCCCGCATCCCGCATTATCCCGCCATCCCGCGCCATCCCGCTAAGTCATCCCGCCATCCCGCTCATCCCGCTCTCGATCCCGCGCATATCCCGCAAATCCCGCATCCCGCATCCCGCGGAAGTAGATCCCGCAATCCCGCATCCCGCATCCCGCCGATCCCGCCTATATCCCGCATCCCGCAACATCCCGCGGCATCCCGCTCGTCCGATCCCGCATCCCGCCTTCATCCCGCCATATCCCGCCTACATCCCGCCATCCCGCTTCGCCCCTATCCCGCATCCCGCTCAAATCCCGCTCATCCCGCATCCCGCTATCCCGC'
s='ATCCCGCAT'
length = len(s)
count = 0
for l in range(len(S)-len(s)):
    if S[l:l+length] == s:
        count += 1
print count