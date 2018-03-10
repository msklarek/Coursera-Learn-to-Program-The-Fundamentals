def convert_to_celsius(temp):
    '''(number) -->float
    Return the number of Celsius degrees equivalent to fahrenheit degrees
    
    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''
    return (temp -32) *5 / 9

