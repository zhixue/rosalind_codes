def fun(s,k):
    possible_result = []
    for i in range(len(s)-k):
        possible_result.append(s[i:i+k])
    possible_result = [x for x in set(possible_result)]
    max_flag = ''
    max_number = 0
    for one in possible_result:
        count = 0
        for l in range(len(s)-k):
            if s[l:l+k] == one:
                count += 1
        if count >= max_number:
            max_number = count
            print one,


stri = 'CCGGCCGTCCGGCCGTGGTGACAAAAAAGATGCCGGCCGTTTCGACTCCGTGGCTGGGTGACACCGGCCGTAAAAAGATGCCGGCCGTCCGTGGCTGAAAAAGATGAAAAAGATGCCGGCCGTGGTGACATTCGACTAAAAAGATGTTCGACTCCGTGGCTGCCGGCCGTTTCGACTAAAAAGATGAAAAAGATGTTCGACTAAAAAGATGGGTGACATTCGACTGGTGACAGGTGACAGGTGACACCGTGGCTGCCGGCCGTAAAAAGATGGGTGACAAAAAAGATGAAAAAGATGTTCGACTCCGGCCGTTTCGACTTTCGACTGGTGACACCGGCCGTTTCGACTCCGTGGCTGCCGTGGCTGCCGGCCGTGGTGACAGGTGACACCGTGGCTGAAAAAGATGTTCGACTCCGTGGCTGCCGTGGCTGAAAAAGATGTTCGACTCCGTGGCTGCCGTGGCTGCCGGCCGTCCGGCCGTGGTGACAGGTGACACCGTGGCTGCCGTGGCTGGGTGACAAAAAAGATGAAAAAGATGAAAAAGATGCCGTGGCTGTTCGACTAAAAAGATGGGTGACACCGTGGCTGCCGTGGCTGTTCGACTGGTGACATTCGACTCCGTGGCTGCCGTGGCTGCCGGCCGTCCGGCCGTTTCGACTCCGTGGCTGTTCGACTTTCGACTCCGTGGCTGCCGGCCGTGGTGACATTCGACTCCGGCCGTCCGTGGCTGCCGTGGCTGTTCGACTGGTGACACCGTGGCTGCCGTGGCTGCCGTGGCTGTTCGACTCCGTGGCTGGGTGACACCGGCCGTGGTGACACCGGCCGTAAAAAGATGGGTGACA'
fun(stri,14)