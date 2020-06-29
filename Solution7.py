#function that takes list of words and return length of longest one

def longest_str_len(list1):
    list1_len = []
    
    for n in list1:
        list1_len.append((len(n),n))
    list1_len.sort()
    print(list1_len[-1][1])
    return len(list1_len[-1][1])

print(longest_str_len(["seen","python","good","hello world"]))

