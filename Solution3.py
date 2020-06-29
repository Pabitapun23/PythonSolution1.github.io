#change first character of string when repeat again with $

def replace_first_char(strs):
    char = strs[0]

    strs = strs.replace(char,'$')
    strs = char + strs[1:]

    return strs

print(replace_first_char('restart'))