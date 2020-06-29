#remove the characters which have odd index value

def remove_odd_index_char(str1):
    chars = ""
    for i in range(len(str1)):
        if i % 2 == 0:
            chars = chars + str1[i]
    return chars

print(remove_odd_index_char('python'))
print(remove_odd_index_char('program'))



