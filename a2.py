def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return (get_length(dna1) > get_length(dna2))

    


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    chars = 0
    for char in dna:
        if char in nucleotide:
            chars=chars +1
    return chars


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    if dna1.find(dna2) > 0:
        return True

    return False

def is_valid_sequence(dna):
    '''(str)->bool

    Return True if and only if DNA sequence dna includes only characters 'A'
    'T', 'C' or 'G'.

    >>>is_valid_sequence('AGT')
    True
    >>>is_valid_sequence('AGt')
    False
    '''
    is_valid=True
    valid_string='ATCG'

    for char in dna:
        if char not in valid_string:
            return False
    return is_valid


def insert_sequence(dna1,dna2,num):
    '''(str,str,int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence
    dna2 into the first DNA sequence dna1 at the given index num.
    
    >>>insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>>insert_sequence('ATGT','GT', -1)
    'ATGGTT'
    '''

    return dna1[0:num] + dna2 +dna1[num:]

def get_complement(str):
    '''(str)-> str
    Return the nucleotide's complement to str. str can be only 'A', 'T',
    'C' or 'G'.
    >>>get_complement('A')
    T
    >>>get_cemplemeny('C')
    '''
    for char in str:
        if char in 'A':
            return 'T'
        if char in 'T':
            return 'A'
        if char in 'C':
            return 'G'
        if char in 'G':
            return 'C'
    return 'not_valid'

def get_complementary_sequence(str):

    '''(str)->str
    Return the DNA sequence that is compplementary to the given DNA sequence str.
    >>>get_complementary_sequence('AGTC')
    'TCAG'
    >>>get_complementary_sequence('AATT')
    'TTAA'
    '''
    new_sequence= ''

    for char in str:
        new_sequence= new_sequence + get_complement(char)
    return new_sequence
    return ('not valid')
