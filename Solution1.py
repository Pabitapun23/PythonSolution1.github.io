#Count no. of char in string

def count_char(strings):
    dict = {}

    for n in strings:
        keys = dict.keys() 
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(count_char('google.comkk'))