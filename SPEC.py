table = {
    'A':   71.03711,
'C':   103.00919,
'D':  115.02694,
'E':   129.04259,
'F':   147.06841,
'G':   57.02146,
'H':   137.05891,
'I':   113.08406,
'K':   128.09496,
'L':   113.08406,
'M':   131.04049,
'N':   114.04293,
'P':   97.05276,
'Q':   128.05858,
'R':   156.10111,
'S':   87.03203,
'T':   101.04768,
'V':   99.06841,
'W':   186.07931,
'Y':   163.06333
}

l = 0
diff_mass = []
for line in open('rosalind_spec.txt'):
    l += 1
    if l > 1:
        temp_small = temp_big
    temp_big = float(line.rstrip())
    if l > 1:
        diff_mass.append(temp_big-temp_small)
print diff_mass

seq = ''
for one in diff_mass:
    for key,value in table.items():
        if abs(value - one) < 0.025:
            seq += key
            break
print seq