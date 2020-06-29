#Replacing the strings

def replace_not_poor_str(str1):
    str_not = str1.find('not')
    str_poor = str1.find('poor')

    if str_not < str_poor and (str_not>0 and str_poor>0):
        return str1.replace(str1[str_not:(str_poor+4)],'good')
       
    return str1

print(replace_not_poor_str('The lyrics is not that poor!'))
print(replace_not_poor_str('The lyrics is poor!'))