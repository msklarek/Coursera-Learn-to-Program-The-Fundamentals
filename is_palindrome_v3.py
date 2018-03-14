def is_palindrome_v3(s):
    '''(str) -> bool

    Return True if and only if s is palindrome.
    
    >>>is_palindrome_v3('noon')
    True
    >>>is_palindrome_v3('racecar')
    True
    >>>is_palindrome_v3('dented')
    False
    '''
    n = len(s)
    i = 1
    for char in s:
        if char == s[n - i]:
            i = i+1
        else:
            return False
    return True
        
            
