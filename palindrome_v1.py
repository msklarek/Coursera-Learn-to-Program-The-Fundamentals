def is_palindrome_v1(s):
    '''(str) -> bool

    Return True if and only if s is palindrome.
    
    >>>is_palindrome_v1('noon')
    True
    >>>is_palindrome_v1('racecar')
    True
    >>>is_palindrome_v1('dented')
    False
    '''
    return word == s

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
    

