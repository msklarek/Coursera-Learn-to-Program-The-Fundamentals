def is_even(num):
    '''(int) -> bool
    Return wheather num is even.
    
    >>>is_even(4)
    True
    >>>is_even(77)
    False
    '''
    return num % 2 == 0
##    if num % 2 == 0:
##        return True
##    else:
##        return False

def same_abs(num1, num2):
    ''' (number, number) -> bool
    Return True if and only if num1 and num2 have the same absolute value.
    >>> same_abs(12.5, -12.5)
    True
    >>> same_abs(3, 4.5)
    False
    '''
    return abs(num1) == abs(num2)
##    if abs(num1) == abs(num2):
##        return True
##    else:
##        return False

def inhospitable_weather(temp):
    ''' (number) -> bool
    Return True if and only if the given temperature in degrees Celsius is unpleasant (too hot or too cold).
    >>> inhospitable_weather(20)
    False
    '''
    return temp > 28 or temp < 12 !=0
##    
##    if temp > 28:
##        return True
##    elif temp < 12:
##        return True
##    else:
##        return False
