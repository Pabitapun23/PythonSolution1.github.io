#Count the occurence of each word in a sentence

def count_word(str1):
    strings = dict()
    sent = str1.split()

    for word in sent:
        if word in strings:
            strings[word] += 1
        else:
            strings[word] = 1
    
    return strings

print(count_word('this is a python program and this is good'))

