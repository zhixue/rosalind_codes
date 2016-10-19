s= open('rosalind_ba1f.txt').read()

min_mark = 0
flag = 0
now_mark = 0
print len(s)
for i in range(len(s)):
    if s[i] == 'C':
        now_mark -= 1
        if now_mark <= min_mark:
            min_mark = now_mark
            flag = i
            print min_mark,flag+1
    if s[i] == 'G':
        now_mark += 1
