#swapping first 2 characters of the string and then join them with space

def swap_join_char(str1,str2):
    newStr1 = str2[:2] + str1[2:]
    newStr2 = str1[:2] + str2[2:]

    return newStr1 + ' ' + newStr2

print(swap_join_char('abc','xyz'))
