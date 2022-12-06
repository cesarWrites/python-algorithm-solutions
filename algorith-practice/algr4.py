"""Write a python program to compute the sum of the three integers. If one of the values is 13 then do not count it and its right towards the sum."""
def compute_sum(x,y,z):
    sum = x + y + z
    if(x == 13):
        sum = 0
        return sum
    elif(y == 13):
        sum = x
        return sum
    else:
        return sum
print(compute_sum(4,5,7))
print(compute_sum(7,4,12))
print(compute_sum(10,13,12))
print(compute_sum(13, 12, 18))

def compute_sum(x,y,z):
    sum = x + y + z
    if(x == 13):
        sum = 0
        return sum
    elif(y == 13):
        sum = x
        return sum
    else:
        return sum
print(compute_sum(4,5,7))
print(compute_sum(7,4,12))
print(compute_sum(10,13,12))
print(compute_sum(13, 12, 18))

"""Write a python program to compute the sum of the three given integers. However, if any of the values is in the range 10..20 inclusive then that value counts as 0, except 13 and 17."""
def compute_sum(x,y,z):
    sum = x + y + z
    if(x >=10 and x <= 20):
        sum = 0 + y + z
    elif(y >=10 and y <= 20):
        sum = x + 0 + z
        return sum
    elif(z >= 10 and z <= 20):
        sum = x + y + 0
        return sum
    else:
        return sum
print(compute_sum(4,5,7))
print(compute_sum(7,4,12))  
print(compute_sum(10,13,12)) 

""" Write a python program to check two given integers and return the value whichever value is nearest to 13 without going over. Return 0 if both numbers go over."""
def check_integers(x,y):
    while ((x <= 13) and (y <= 13)):
        if((13 -x) > (13 -y)):
            return y
        elif((13-x) < (13 -y)):
            return x
    return 0
print(check_integers(4,5))
print(check_integers(7,12)) 
print(check_integers(10,13))
print(check_integers(17,33))

""" Write a python program to check three given integers (small, medium and large) and return true if the difference between small and medium and the difference between medium and large is same."""
def check_integers(small,medium,large):
    if((small - medium) == (medium - large)):
        return True
    return False
print(check_integers(4,5,6))
print(check_integers(7,12,13))
print(check_integers(-1, 0, 1))

"""Write a python program to create a new string using two given strings s1, s2, the format of the new string will be s1s2s2s1."""
def create_new_string(s1,s2):
    return s1 + s2 + s2 + s1
print(create_new_string("Hi", "Hello"))
print(create_new_string("whats", "app"))

#6 th December 2022
"""Write a python program to insert a given string into middle of the another given string of length 4."""
def insert_string(str1, str2):
    s = list(str1)
    s.insert(2, str2)
    s2 = ''.join(s)
    return s2
print(insert_string("[[]]","Hello"))
print(insert_string("(())", "Hi"))

""" Write a python program to create a new string using three copies of the last two character of a given string of length atleast two."""
def create_new_string(str1):
    while(len(str1) >= 2):
        s = str1[-2:]
        return s + s + s
print(create_new_string("Hello"))
print(create_new_string("Hi"))
print(create_new_string("Good"))

"""Write a python program to create a new string using first two characters of a given string. If the string length is less than 2 then return the original string."""
def create_new_string(str1):
    if(len(str1) >= 2):
        s = str1[0:2]
        return s
    return str1
print(create_new_string("Hello"))
print(create_new_string("Hi"))
print(create_new_string("H"))

"""Write a python program to create a new string of the first half of a given string of even length"""
def create_new_string(str1):
     s_length = int(len(str1) / 2)
     s = str1[0:s_length]
     return s
print(create_new_string("Hi"))
print(create_new_string("HTML"))
print(create_new_string("python"))

"""Write a python program to create a new string without the first and last character of a given string of length atleast two. """
def create_new_string(str1):
    s = str1[1:-1]
    return s
print(create_new_string("Hello"))
print(create_new_string("Hi"))
print(create_new_string("python"))

"""Write a python program to create a new string from two given string one is shorter and another is longer. The format of the new string will be long string + short string + long string"""
def create_new_string(str1,str2):
    s1 = len(str1)
    s2 = len(str2)
    if(s1 > s2):
        return str1 + str2 + str1
    else:
        return str2 + str1 + str2
print(create_new_string("Hello", "Hi"))
print(create_new_string("JS", "Python"))  

"""Write a python program to concat two given string of length atleast 1, after removing their first character."""
def concat_strings(str1, str2):
    if((len(str1) >= 1) and (len(str2) >=1)):
        s1 = str1[1:]
        s2 = str2[1:]
        return s1 + s2
print(concat_strings("Hello", "Hi"))
print(concat_strings("JS", "Python"))

"""Write a python program to move the first two characters to the end of a given string of length at least two."""
def move_string_characters(str1):
    if(len(str1) >= 2):
        s = str1[0:2]
        s1 = str1[2:]
        return s1 + s
print(move_string_characters("Hello"))
print(move_string_characters("JS"))
print(move_string_characters("python"))

"""Write a python program to move the last two characters to the start of a given string of length at least two."""
def move_string_characters(str1):
    if(len(str1) >= 2):
        s = str1[:-2]
        s1 = str1[-2:]
        return s1 + s
print(move_string_characters("Hello"))
print(move_string_characters("JS"))

"""Write a python program to create a new string without the first and last character of a given string of any length."""
def create_new_string(str1):
    s = str1[1:-1]
    return s
print(create_new_string("Hello"))
print(create_new_string("JS"))

"""Write a python program to create a new string using the two middle characters of a given string of even length (at least 2)."""
def create_new_string(str1):
    if((len(str1) >= 2) and (len(str1) %2 == 0)):
        s1 = str1[int(len(str1) / 2 -1)]
        s2 = str1[int(len(str1) /2)]
        return s1 + s2
print(create_new_string("Java"))
print(create_new_string("Hell"))
print(create_new_string("JS"))
print(create_new_string("python"))
"""Write a python program to check if a given string ends with 'on'"""
def check_string(str1):
    s = str1[-2:]
    return s
print(check_string("Hello"))
print(check_string("python"))
print(check_string("on"))
print(check_string("o"))

"""Write a python program to create a new string using the first and last n characters from a given string of length at least n."""
def create_new_string(str1,n):
    s1 = str1[0:n]
    s2 = str1[-n:]
    return s1 + s2
print(create_new_string("Hello", 1))
print(create_new_string("Python", 2))
print(create_new_string("On", 1))

"""Write a python program to create a new string of length 2 starting at the given index of a given string."""
def create_new_string(str1, n):
    s = str1[n:n+2]
    return s
print(create_new_string("Hello", 1))
print(create_new_string("Python", 2))
print(create_new_string("on", 0)) 

""" Write a python program to create a new string taking 3 characters from the middle of a given string at least 3."""
def create_new_string(str1):
    if((len(str1) >= 3) and len(str1) % 2 == 0):
        s1 = str1[len(str1) / 2 -1]
        s2 = str1[len(str1) / 2 ]
        s3 = str1[len(str1) / 2 + 1]
        return s1 + s2 + s3
print(create_new_string("Hello"))
"""Write a python program to check if a given string ends with 'on'"""
def check_string(str1):
    s = str1[-2:]
    return s
print(check_string("Hello"))
print(check_string("python"))
print(check_string("on"))
print(check_string("o"))

"""Write a python program to create a new string using the first and last n characters from a given string of length at least n."""
def create_new_string(str1,n):
    s1 = str1[0:n]
    s2 = str1[-n:]
    return s1 + s2
print(create_new_string("Hello", 1))
print(create_new_string("Python", 2))
print(create_new_string("On", 1))
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""Write a python program to create a new string of length 2, using first two characters of a given string. If the given string length is less than 2 use '#' as missing characters. """
def create_new_string(str1):
    if(len(str1) <2):
        return str1 + "#"
    return str1[0:2]
print(create_new_string("Hello"))
print(create_new_string("Python"))
print(create_new_string("a"))
print(create_new_string(""))

"""Write a python program to create a new string taking the first character from a given string and the last character from another given string. If the length of any given string is 0, use '#' as its missing character. """
def create_new_string(str1,str2):
    if(len(str1) == 0):
        s1 = '#'
        s2 = str2[-1]
        return s1 + s2
    elif(len(str2) == 0):
        s1 = str1[0]
        s2 = '#'
        return s1 + s2
    else:
        return str1[0] + str2[-1]
print(create_new_string("Hello", "Hi"))
print(create_new_string("Python", "PHP"))
print(create_new_string("JS", "JS"))
print(create_new_string("Csharp", ""))

"""Write a python program to concat two given strings (lowercase). If there are any double character in new string then omit one character."""
def concat_strings(str1,str2):
    s = str1.lower() + str2.lower()
    return s
print(concat_strings("abc", "cat"))
    
