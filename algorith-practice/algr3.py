"""Write a python program to find the larger value from two positive integer values that is in the range 20..30 inclusive, or return 0 if neither is in that range"""
def check_larger_value(x,y):
    if((x>=20 and x <= 30) or (y>=20 and y<=30)):
        if(x>y):
            return x
        else:
            return y
    return 0
print(check_larger_value(78,95))
print(check_larger_value(20,30))
print(check_larger_value(21,25))
print(check_larger_value(28,28))

"""Write a python program to check if a given string contains between 2 and 4 'z' character."""
def check_z_character(str1):
    if ((str1.count('z') >=2) and (str1.count('z') <=4)):
        return True
    return False
print(check_z_character("frizz"))
print(check_z_character("zane"))
print(check_z_character("Zazz"))
print(check_z_character("false"))

"""Write a python program to check if two given non-negative integers have the same last digit."""

def check_last_digit(x,y):
    if x>0 and y>0:
        if(x % 10 == y % 10):
            return True
        return False
print(check_last_digit(123,456))
print(check_last_digit(12,512))
print(check_last_digit(7,87))
print(check_last_digit(12,45))

"""Write a python program to convert the last 3 characters of a given string in upper case. If the length of the string has less than 3 then uppercase all the characters."""
def convert_to_uppercase(str1):
    s = str1[-3:]
    if(len(str1) >= 3):
        return str1.replace(s, '') + s.upper()
    elif(len(str1) <3):
        return str1.upper()
print(convert_to_uppercase("python"))
print(convert_to_uppercase("py"))
print(convert_to_uppercase("PHP"))
print(convert_to_uppercase("JS"))  

"""python program to check if phone number begins with country code 254"""
def check_phone_number(phone_no):
    s = phone_no[0:3]
    if(s == "254" and len(phone_no) == 12):
        return phone_no
    else:
        return "enter correct phone number"
print(check_phone_number("0780952134"))
print(check_phone_number("254704569063"))
print(check_phone_number("2547345678"))
print(check_phone_number("254734567896"))

"""Write a python program to create a new string which is n (non-negative integer) copies of a given string"""
def create_new_string(str1, n):
    if(n > 0):
        return str1 * n
print(create_new_string("JS", 2))
print(create_new_string("JS", 3))
print(create_new_string("JS", 1))

"""Write a python program to create a new string which is n (non-negative integer) copies of the the first 3 characters of a given string. If the length of the given string is less than 3 then return n copies of the string"""
def create_new_string(str1, n):
    if (n > 0):
        s = str1[0:3]
        return s * n
print(create_new_string("python",2))
print(create_new_string("python",3))
print(create_new_string("JS",2))

""" ** (pending) Write a python program to count the string "aa" in a given string and assume "aaa" contains two "aa"""
def count_string(str1):
    return str1.count("aa")
print(count_string("bbaaccaag"))

"""Write a python program to check if the first appearance of "a" in a given string is immediately followed by another "a"""
def check_appearance_of_string(str1):
    s = str1.find("a")
    while s <= len(str1):
            s + 1
            if(str1[s] == str1[s + 1]):
                return True
            return False
print(check_appearance_of_string("caabb"))
print(check_appearance_of_string("babaaba")) 
print(check_appearance_of_string("aaaaa"))

""". Write a python program to create a new string made of every other character starting with the first from a given string"""
def new_string(str1):
    s = str1[0]
    n = 0
    for n in len(str1):
        if(n % 2 == 0):
            return s + str1[n]
print(new_string("Python"))
print(new_string("PHP"))

"""Write a python program to create a string like "aababcabcd" from a given string "abcd"""  
def check_specific_number(arr1, num):
    for num in arr1:
        return True
print(check_specific_number([1,2,9,3], 3))

"""Write a python program to check if one of the first 4 elements in an array of integers is equal to a given element."""
def check_equal_integer(arr1,num):
    new_arr = arr1[0:4]
    for num in new_arr:
        return True
    return False
print(check_equal_integer([1,2,3,4,5,6],2))

"""Write a python program to check whether the sequence of numbers 1, 2, 3 appears in a given array of integers somewhere"""
def check_sequence_of_numbers(arr1):
    s = []
    for s in arr1:
        if(s == (1,2,3)):
            return True
        return False
    
print(check_sequence_of_numbers([1,1,2,3,1]))
print(check_sequence_of_numbers([1,1,2,4,1]))

""" Write a PHP program to compute the sum of the two given integers. If the sum is in the range 10..20 inclusive return 30."""
def sum_of_integers(x,y):
    z = x + y
    if(z >= 10 and z <= 20):
        return 30
    return z
print(sum_of_integers(12,17))
print(sum_of_integers(2,17))
""" Write a python program that accept two integers and return true if either one is 5 or their sum or difference is 5."""
def sum_of_integer(x,y):
    if((x == 5 or y == 5) or ( x + y == 5) or (x - y == 5)):
        return True
    return False
print(sum_of_integer(5,4))
print(sum_of_integer(4,3))
print(sum_of_integer(4,1))

def test_number(n):
    if(n > 0):
        if((n % 13 == 0) or ((n - 1) %13 == 0)):
            return True
        return False
print(test_number(13))
print(test_number(14))
print(test_number(27))
print(test_number(41))

"""Write a python program to check if a given non-negative given number is a multiple of 3 or 7, but not both."""
def check_multiples(n):
    if(n>0):
        if((n % 3 == 0) or (n % 7 == 0)):
            return int(1)
        return int(0)
print(check_multiples(3))
print(check_multiples(7))
print(check_multiples(21))
print(check_multiples(29))

"""Write a python program to check if a given number is within 2 of a multiple of 10."""
def check_multiples(n):
    if(((n % 10) == 0) or ((n + 2) % 10 == 0) or ((n -2) %10 ==0)):
        return True
    return False
print(check_multiples(3))
print(check_multiples(7))
print(check_multiples(8))
print(check_multiples(10))

"""Write a python program to compute the sum of the two given integers. If one of the given integer value is in the range 10..20 inclusive return 18."""
def compute_sum(x,y):
    if((x >= 10 and x <= 20) or (y >=10 and y <= 20)):
        return 18
    return x + y
print(compute_sum(3,7))
print(compute_sum(10,11))
print(compute_sum(10,20))
print(compute_sum(21,220))

"""Write a python program to check whether a given string starts with "F" or ends with "B". If the string starts with "F" return "Fizz" and return "Buzz" if it ends with "B" If the string starts with "F" and ends with "B" return "FizzBuzz". In other cases return the original string."""
def string_starts_with(str1):
    s = str1[0]
    s1 = str1[-1]
    if(s == 'F'):
        return "Fizz"
    elif(s1 == 'B'):
        return "Buzz"
    elif((s == "F") and (s1 == "B")):
        return "FizzBuzz"
    else:
        return str1
print(string_starts_with("FizzBuzz"))
print(string_starts_with("Founder"))
print(string_starts_with("Buzz"))
print(string_starts_with("RIB"))
print(string_starts_with("Try"))

"""Write a python program to check if it is possible to add two integers to get the third integer from three given integers."""
def add_integers(x,y,z):
    if((x + y) == z):
        return True
    return False
print(add_integers(1,2,3))
print(add_integers(4,5,6))
print(add_integers(-1,1,0))

"""Write a python program to check if y is greater than x, and z is greater than y from three given integers x,y,z."""
def check_greater_integer(x,y,z):
    if((x < y) and (z > y)):
        return True
    return False
    
print(check_greater_integer(1, 2, 3))
print(check_greater_integer(4, 5, 6))
print(check_greater_integer(-1, 1, 0))
"""Write a python program to check if two or more non-negative given integers have the same rightmost digit."""
def check_numbers(x,y,z):
    if(((x % 10) == (y % 10)) or(y % 10 == z % 10) or (x % 10 == z % 10)):
        return True
    return False
print(check_numbers(11, 21, 31))
print(check_numbers(11, 22, 31))
print(check_numbers(11, 22, 33))
"""Write a python program to compute the sum of two given non-negative integers x and y as long as the sum has the same number of digits as x. If the sum has more digits than x then return x without y."""
def add_numbers(x,y):
    sum = x + y
    if((len(str(sum))) == len(str(x))):
        return sum
    else:
        return x
print(add_numbers(4,5))
print(add_numbers(7,4))
print(add_numbers(10,10))

"""Write a python program to compute the sum of three given integers. If the two values are same return the third value. """
def compute_sum(x,y,z):
    sum = x + y + z
    if(x == y):
        return z
    return sum
print(compute_sum(4,5,7))
print(compute_sum(7,4,12))
print(compute_sum(10,10,12))
print(compute_sum(12,12,18))
