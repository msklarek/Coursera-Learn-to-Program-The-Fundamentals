import palindrome_v1


def is_palindrome_v2(s):
    '''(str) -> bool

    Return True if and only if s is palindrome.
    
    >>>is_palindrome_v2('noon')
    True
    >>>is_palindrome_v2('racecar')
    True
    >>>is_palindrome_2('dented')
    False
    '''
    # The number of chars in s.
    n = len(s)

    # Compare the first half of s to reverse of the second half.
    # Omit the middle character of an old-lengthstring.
    return s[:n//2] == palindrome_v1reverse(s[n - n // 2:])

print('In version 2, the module name is ', __name__)
