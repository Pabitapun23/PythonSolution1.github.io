#change in string

def modify_string(str1):
    if len(str1)>=3:
        if str1[-3:] == 'ing':
            return str1 + 'ly'
        else:
            return str1 + 'ing'
      
    return str1

print(modify_string('abc'))
print(modify_string('ab'))
print(modify_string('string'))