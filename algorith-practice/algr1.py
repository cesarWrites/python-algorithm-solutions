"""Write a Python program to compute the sum of the two given integer values. 
If the two values are the same, then returns triple their sum"""
def sum_of_integers(a,b):
    if (a == b):
        return (a + b) * 3
    else:
        return (a + b)
print(sum_of_integers(1,2))
print(sum_of_integers(3,2))
print(sum_of_integers(2,2))


"""2. Write a python program to get the absolute difference between n and 51. 
If n is greater than 51 return triple the absolute difference."""

def absolute_difference(n):
    if (n > 51):
        return (n - 51) * 3
    else:
        return(51 - n)
print(absolute_difference(53))
print(absolute_difference(30))
print(absolute_difference(51))

"""Write a python program to check two given integers, and return true if one of them is 30 or if their sum is 30. Go to the editor
Sample Input:"""
def check_two_integers(x,y):
    if((x == 30) or (y == 30) or (x + y == 30)):
        return True
    return False
print(check_two_integers(30,0))
print(check_two_integers(25,5))
print(check_two_integers(20,30))
print(check_two_integers(20,25))

""" Write a python program to check a given integer and return true if it is within 10 of 100 or 200. Go to the editor
Sample Input:"""
def check_integer_range(n):
    if(abs(n - 100) <= 10 or abs(n - 200) <= 10):
        return True
    return False
print(check_integer_range(103))
print(check_integer_range(90))
print(check_integer_range(89))

""" Write a python program to create a new string where 'if' is added to the front of a given string. 
If the string already begins with 'if', return the string unchanged."""
def create_new_string(str1):
    s = str1[0:2]
    if(s == "if"):
        return str1
    return "if" + " " + str1
print(create_new_string("if else"))
print(create_new_string("else"))
print(create_new_string("if"))

"""Write a python program to remove the character in a given position of a given string. 
The given position will be in the range 0..string length -1 inclusive"""
def remove_character(str1, pos):
    s = str1[0:pos]
    return s
print(remove_character("Python", 1))
print(remove_character("Python", 0))
print(remove_character("Python", 4))

"""Write a python program to exchange the 
first and last characters in a given string and return the new string"""
