with open('rosalind_ba10c.txt') as f:
    i = 0

    pa = ''
    st = ''#unknwon
    s = {}
    p = {}
    for line in f:
        i += 1
        if i == 1:
            path = line.rstrip()




        #state matrix
        if i == 8:
            s['AA'] = float(line.rstrip().split()[1])
            s['AB'] = float(line.rstrip().split()[2])
            s['AC'] = float(line.rstrip().split()[3]) #3
        if i == 9:
            s['BA'] = float(line.rstrip().split()[1])
            s['BB'] = float(line.rstrip().split()[2])
            s['BC'] = float(line.rstrip().split()[3])  # 3
        if i == 10:  # 3
            s['CA'] = float(line.rstrip().split()[1])  # 3
            s['CB'] = float(line.rstrip().split()[2])  # 3
            s['CC'] = float(line.rstrip().split()[3])  # 3
        #path&state matrix
        if i == 13:
            p['Ax'] = float(line.rstrip().split()[1])
            p['Ay'] = float(line.rstrip().split()[2])
            p['Az'] = float(line.rstrip().split()[3])
        if i == 14:
            p['Bx'] = float(line.rstrip().split()[1])
            p['By'] = float(line.rstrip().split()[2])
            p['Bz'] = float(line.rstrip().split()[3])
        if i == 15:
            p['Cx'] = float(line.rstrip().split()[1])
            p['Cy'] = float(line.rstrip().split()[2])
            p['Cz'] = float(line.rstrip().split()[3])

    maxp_m = [] #possiblity matrix
    maxt_m = [] #trace matrix
    for k in range(len(path)):
        if k == 0:
            a = 1 / 2 * p['A' + path[k]]
            b = 1 / 2 * p['B' + path[k]]
            c = 1 / 2 * p['C' + path[k]]
            maxp_m.append([a,b,c])
            maxt_m.append(['A','B','C'])
            if a > b:
                st = 'A'
            else:
                st = 'B'
            if c > max(a,b):
                st = 'C'
        else:
            # this state is A
            aa = maxp_m[k - 1][0] * s['AA'] * p['A' + path[k]]
            ba = maxp_m[k - 1][1] * s['BA'] * p['A' + path[k]]
            ca = maxp_m[k - 1][2] * s['CA'] * p['A' + path[k]]
            if aa >= ba:
                toA = aa
                temptraceA = maxt_m[k-1][0] + 'A'
            else:
                toA = ba
                temptraceA = maxt_m[k - 1][1] + 'A'
            if ca > max(aa,ba):
                toA = ca
                temptraceA = maxt_m[k - 1][2] + 'A'

            # this state is B
            ab = maxp_m[k - 1][0] * s['AB'] * p['B' + path[k]]
            bb = maxp_m[k - 1][1] * s['BB'] * p['B' + path[k]]
            cb = maxp_m[k - 1][2] * s['CB'] * p['B' + path[k]]
            if ab >= bb:
                toB = ab
                temptraceB = maxt_m[k - 1][0] + 'B'
            else:
                toB = bb
                temptraceB = maxt_m[k - 1][1] + 'B'
            if cb > max(ab,bb):
                toB = cb
                temptraceB = maxt_m[k - 1][2] + 'B'

             # this state is C
            ac = maxp_m[k - 1][0] * s['AC'] * p['C' + path[k]]
            bc = maxp_m[k - 1][1] * s['BC'] * p['C' + path[k]]
            cc = maxp_m[k - 1][2] * s['CC'] * p['C' + path[k]]
            if ac >= bc:
                toC = ac
                temptraceC = maxt_m[k - 1][0] + 'C'
            else:
                toC = bc
                temptraceC = maxt_m[k - 1][1] + 'C'
            if cc > max(ac, bc):
                toC = cc
                temptraceC = maxt_m[k - 1][2] + 'C'

            maxp_m.append([toA, toB,toC])
            maxt_m.append([temptraceA,temptraceB,temptraceC])


    u =len(maxp_m)-1
    if maxp_m[u][0] >= maxp_m[u][1]:
        if maxp_m[u][2] > maxp_m[u][0]:
            print(maxt_m[u][2])
        else:
            print(maxt_m[u][0])
    else:
        print(maxt_m[u][1])










