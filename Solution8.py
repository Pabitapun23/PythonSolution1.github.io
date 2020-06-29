#remove nth index character from non-empty string

def char_removal(str1, n):
    start_str1 = str1[:n]
    end_str1 = str1[n+1:]

    return start_str1 + end_str1

print(char_removal('program', 1))
print(char_removal('program', 2))
print(char_removal('program', 4))
print(char_removal('program', 0))
