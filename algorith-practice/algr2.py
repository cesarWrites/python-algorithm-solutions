"""Write a python program to create a new string taking the first 3 characters of a given string and return the string with the 3 characters added at both the front and back. If the given string length is less than 3, use whatever characters are there."""
def create_new_string(str1):
    s = str1[0:3]
    if(len(str1) >= 3):
        str1 = s + str1 + s
        return str1
    else:
        return str1 + str1 + str1
print(create_new_string("python"))
print(create_new_string("JS"))
print(create_new_string("Code"))

"""Write a python program to check if a given string starts with 'C#' or not."""
def check_first_string_char(str1):
    s = str1[0:2]
    if(s == 'C#'):
        return True
    return False
print(check_first_string_char("C#50"))
print(check_first_string_char("Python"))

"""Write a python program to check if one given temperatures is less than 0 and the other is greater than 100"""
def check_temperature(x,y):
    if((x > 100 and y < 0) or (x < 0 and y > 100)):
        return True
    return False
print(check_temperature(120,-1))
print(check_temperature(-1,120))
print(check_temperature(120,2))

"""Write a python program to check two given integers whether either of them is in the range 100..200 inclusive."""
def check_range_of_integers(x,y):
    if((x >=100 and x <= 200) or (y >= 100 and y <= 200)):
        return True
    return False
print(check_range_of_integers(100,199))
print(check_range_of_integers(250,300))
print(check_range_of_integers(105,190))
  
"""Write a python program to check whether three given integer values are in the range 20..50 inclusive. Return true if 1 or more of them are in the said range otherwise false""" 
def check_integer_values(nums = []):
    for num in nums:
        if(num >= 20 and num <= 50):
            return True
        return False
print(check_integer_values(nums = [11, 20, 12]))
print(check_integer_values(nums = [30, 30, 25]))
print(check_integer_values(nums = [25, 35, 50]))
print(check_integer_values(nums = [15, 12, 8]))

"""Write a python program to check if a string 'yt' appears at index 1 in a given string. 
If it appears return a string without 'yt' otherwise return the original string."""
def check_string(str1):
    s = str1[1:3]
    if(s == 'yt'):
        return str1[2:]
    return str1
print(check_string("python"))
print(check_string("java"))

"""Write a python program to check the largest number among three given integers"""
def check_largest_number(x,y,z):
    if(x > y):
        return "x is largest number"
    elif(y>z):
        return "y is largest"
    else:
        return "z is largest"
print(check_largest_number(23,40,56))
print(check_largest_number(20,46,36))
print(check_largest_number(60,46,36))

"""Write a python program to check which number nearest to the value 100 among two given integers. 
Return 0 if the two numbers are equal. """
def check_nearest_num(x,y):
    n = 100 - x
    m = 100 - y 
    if(n > m):
        return y
    elif(m > n):
        return x
    else:
        return 0
print(check_nearest_num(95,68))
print(check_nearest_num(68,98))
print(check_nearest_num(70,70))
    
"""Write a python program to check whether two given integers are in the range 40..50 inclusive, 
or they are both in the range 50..60 inclusive"""

