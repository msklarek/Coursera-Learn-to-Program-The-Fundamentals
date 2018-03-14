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
    return s[:n//2] == reverse(s[n - n // 2:])

def reverse(s):
    '''(str) - > str
    Return a reversed version of s.

    >>>reverse('hello')
    'olleh'
    '''
    word = ''
    for i in s:
        word = i + word
    return word 
    
