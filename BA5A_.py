def sumtototal(total, coins_list):
    s = [0]
    for i in range(1, total+1):
        s.append(-1)
        for coin_val in coins_list:
            if i-coin_val >=0 and s[i-coin_val] != -1 and (s[i] > s[i-coin_val] or s[i] == -1):
                s[i] = 1 + s[i-coin_val]

    return s[total]


print(sumtototal(16248,[1,3,5,10,11,14,15,19,22]))