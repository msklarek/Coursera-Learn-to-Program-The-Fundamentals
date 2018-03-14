"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>>is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], '')
    False
    """
    i = 0
    while i < len(wordlist):
        if word in wordlist:
            i = i +1
            return True
        else:
            return False


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    """

    word = ''
    i= 0
    while i < len(board[row_index]):
        word = word + board[row_index][i]
        i = i + 1
    return word




def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    """
    #first index change  +1
    #second index stays and its column_index
    word = ''
    for i in range(len(board)):
        word = word + board[i][column_index]
    return word



def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    """
    y = board[0]
    for column_index in range(len(y)):
        if word in make_str_from_column(board, column_index):
            return True

    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>>board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'AX')
    True
    """
    a = board_contains_word_in_column(board, word)
    b = board_contains_word_in_row(board, word)
    if a or b:
        return True
    return False



def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    """
    length = len(word)
    if length < 3:
        return 0
    elif length >= 3 and length <=6:
        score = 1 * len(word)
        return score
    elif length >=7 and length <= 9:
        score = 2 * len(word)
        return score
    elif length >=10:
        score = 3 * len(word)
        return score


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
#counting number of new points for a word
    earned_points = word_score(word)
#adding earned point to old points
    new_points = player_info[1] + earned_points
    player_info[1] = [new_points]    
    


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """
    number = 0
    for word in words:
        if board_contains_word(board, word):
            number = number + 1
    return number


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    lists = []

    for line in words_file:
        word = ''

        for char in line:
            if char != '\n':
                word = word +char
        lists.append(word)
    return lists


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    lists = []

    for line in board_file:
        
#Append characters into sublist
        sub = []
        for char in line:
            
            if char != '\n':
                sub.append(char)

        if sub != []:
            lists. append(sub)

    return lists
