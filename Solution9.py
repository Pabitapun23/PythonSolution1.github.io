#exchange first and last chars of given string

def exchange_str_parts(str1):
    first_str1 = str1[-1:] 
    last_str1 =  str1[:1] 

    #new string
    new_str1 = first_str1 + str1[1:-1] + last_str1

    return new_str1

print(exchange_str_parts('python'))