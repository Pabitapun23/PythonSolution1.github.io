#string having both end characters

def str_program(str1):
    if len(str1)<2:
        return 'Empty string'
    elif len(str1) == 2:
        return str1[0:2]
    else:
        return str1[0:2] + str1[-2:]

print(str_program('python'))
print(str_program('py'))
print(str_program('w'))

