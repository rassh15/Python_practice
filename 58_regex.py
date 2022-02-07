
# to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re

def isallowed(str):

    strfilter = re.compile(r'[a-zA-z0-9]')
    result = strfilter.search(str)

    return bool(result)


# print(isallowed('@#$%'))
# print(isallowed('asdvcvdsd'))

#  program that matches a string that has an a followed by zero or more b's


def iszero(str):
    patterns = 'ab*?'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(iszero('sfasfsaf'))
# print(iszero("ac"))
# print(iszero("abc"))
# print(iszero("abbc"))

#  program that matches a string that has an a followed by one or more b's
def iszero1(str):
    patterns = 'ab+?'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(iszero1('sfasfsaf'))
# print(iszero1("ac"))
# print(iszero1("abc"))
# print(iszero1("abbc"))

#  matches a string that has an a followed by zero or one 'b'
def isallowed1(str):
    
    patterns = 'ab?'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')


# print(isallowed1('sfasfsaf'))
# print(isallowed1("acbccx"))
# print(isallowed1("acbfbb"))
# print(isallowed1("awqx"))

#1 program that matches a string that has an a followed by three 'b'
def ismatched1(str):
    
    patterns = 'ab{3}'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched1('aertda'))
# print(ismatched1('aertdbabbb'))
# print(ismatched1('abbertbbbda'))
# print(ismatched1('abbbertda'))

#2 that matches a string that has an a followed by two to three 'b'

def ismatched2(str):
    
    patterns = 'ab{2,3}'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched2('aertda'))
# print(ismatched2('aertdbabbb'))
# print(ismatched2('abertbbbda'))
# print(ismatched2('abbbertda'))


#3 to find sequences of lowercase letters joined with a underscore

def ismatched3(str):
    
    patterns = '^[a-z]+_[a-z]+$'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched3('aer_tda'))
# print(ismatched3('aertdbabbb'))
# print(ismatched3('abertbbbda'))
# print(ismatched3('abbbertda'))


#4  find the sequences of one upper case letter followed by lower case letters

def ismatched4(str):
    
    patterns = '^[A-Z]+[a-z]+$'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched4('aer_tda'))
# print(ismatched4('aertdbabbb'))
# print(ismatched4('AVtbbbda'))
# print(ismatched4('bberABtda'))

#5 t matches a string that has an 'a' followed by anything, ending in 'b'

def ismatched5(str):
    
    patterns = 'a.*b$'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched5('aer_tda'))
# print(ismatched5('aertdbabbb'))
# print(ismatched5('AVtbbbda'))
# print(ismatched5('bberABtdab'))


#6  program that matches a word at the beginning of a string
def ismatched6(str):
    
    patterns = '^\w+'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched6(' aer_tda'))
# print(ismatched6('abctdbabbb'))
# print(ismatched6('AVtbbbda'))
# print(ismatched6('bbeabcrABtdab'))


#7 program that matches a word at the end of string, with optional punctuation
def ismatched7(str):
    
    patterns = '\w+\S*$'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched7('aer_tda '))
# print(ismatched7('abctdbabbb'))
# print(ismatched7('AVtbbbda'))
# print(ismatched7('bbeabcrABtdab'))

# 8 program that matches a word containing 'z'

def ismatched8(str):
    
    patterns = 'z+'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched8('aer_tda'))
# print(ismatched8('abctdbazbbb'))
# print(ismatched8('AVtbbbda'))
# print(ismatched8('bbeabcrAzBtdab'))

#9 program that matches a word containing 'z', not at the start or end of the word
def ismatched9(str):
    
    patterns = '\Bz\B'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched9('zaertda'))
# print(ismatched9('abctdbazbbb'))
# print(ismatched9('AVtbbbda'))
# print(ismatched9('bbeabcrAzBtdab'))


# 10 program to match a string that contains only upper 
#  and lowercase letters, numbers, and underscores

def ismatched10(str):
    
    patterns = '^[A-Za-z0-9_]*$'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched10('zaertda@'))
# print(ismatched10('abctdbazbbb'))
# print(ismatched10('#$AVtbbbda'))
# print(ismatched10('bbeabcrAzBtdab'))

#  11 program where a string will start with a specific number

def ismatched11(str):
    
    patterns = '^5'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched11('1zaertda'))
# print(ismatched11('5abctdbazbbb'))
# print(ismatched11('23AVtbbbda'))
# print(ismatched11('bbeabcrAzBtdab'))



#12 program to remove leading zeros from an IP address

def ismatched12(str):
    
    ip = str
    string = re.sub('\.[0]*', '.', ip)
    return string

# print(ismatched12("216.08.094.196"))
# print(ismatched12("216.08.004.096"))
# print(ismatched12("216.08.094.106"))
# print(ismatched12("200.08.094.196"))


# 13 check for a number at the end of a string

def ismatched13(str):
    
    patterns = '[0-9]$'
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched13('1zaertda9'))
# print(ismatched13('5abctdbazbbb'))
# print(ismatched13('23AVtbbbda'))
# print(ismatched13('bbeabcrAzBtdab5'))


# 14 rogram to search the numbers (0-9) of length between 1 to 3 in a given string


def ismatched14(str):
    
    patterns = '[0-9]{2,3}'

    res = re.findall(patterns, str)
    print(res)
    if re.search(patterns,  str):
        return 'Found a match!'
    else:
        return('Not matched!')

# print(ismatched14("Exercises number 1, 12, 13, and 345 are important"))

#  Python program to search some literals strings in a string.
# also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'

def ismatched15(str):
    print(str)
    
    patterns = 'fox'

    match = re.search(patterns,  str)
    start = match.start()
    end = match.end()

    print(f'Found a match! at {start} {end}')

# ismatched15('The quick brown fox jumps over the lazy dog.')

#16 Python program to find the substrings within a string. Go to the editor
# Sample text :
# 'Python exercises, PHP exercises, C# exercises'
# Pattern :
# 'exercises'

#  find the occurrence and position of the substrings within a string

def ismatched16(str):
    
    patterns = 'exercises'

    match = re.finditer(patterns,  str)

    for i in match:
        print(f"Found {i.group(0)} {i.end()} {i.start()}")

# ismatched16('Python exercises, PHP exercises, C# exercises')

#  17 replace whitespaces with an underscore and vice versa.
def ismatched17(str):
    
    patterns = ' '

    match = re.sub(patterns, '_',  str)

    print(match)

# ismatched17('Python exercises, PHP exercises, C# exercises')

#18  program to extract year, month and date from an url
def ismatched18(str):
   
    match = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', str)

    print(match)
url = "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
# ismatched18(url)

# 19 convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

def ismatched19(str):
       
    match = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', str)

    print(match)

# ismatched19('2016-09-28')

# 20 match if two words from a list of words starting with letter 'P'

def ismatched20(str):

    for m in str:
        
        match = re.findall(r'(P\w+)\W+(P\w+)', m)
        
        if match:
            print(match)

words = ["Python PHP", "Java JavaScript", "c c++"]

# ismatched20(words)


# 21 program to separate and print the numbers of a given string

def ismatched21(str):
    
    match = re.findall(r'(\d{2,})', str)
    # result = re.split("\D+", text)
    print(match)

# ismatched21("Ten 10, Twenty 20, Thirty 30 ")

#22 find all words starting with 'a' or 'e' in a given string

def ismatched22(str):
    
    match = re.findall(r'[ae]\w+', str)
    print(match)

# ismatched22("abc ert fgt ertvd aesff dfgdg sgsdfg ")

# 23 separate and print the numbers and their position of a given string

def ismatched23(str):
    
    match = re.search(r'\d{2,}', str)

    print(f"Found at {match.start()} value {match.group()}")

# ismatched23("The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly.")

#  24 program to abbreviate 'Road' as 'Rd.' in a given string
def ismatched24(str):

    match = re.sub('Road','Rd',str)

    print(match)

# ismatched24('Road asfa Road')

# 25 replace all occurrences of space, comma, or dot with a colon

def ismatched25(str):
    
    match = re.sub('[ .,]',':',str)

    print(match)

# ismatched25('Road, asfa Road.')

#26 replace maximum 2 occurrences of space, comma, or dot with a colon

def ismatched26(str):
    
    match = re.sub('[ .,]',':',str,2)

    print(match)

# ismatched26('Road, asfa Road.')


# 27 program to find all five characters long word in a string
# find all three, four, five characters long words in a string
#  find all words which are at least 4 characters long in a string
def ismatched27(str):
    
    match1 = re.findall(r'\w{5}',str)
    match2 = re.findall(r'\w{3,5}',str)
    match3 = re.findall(r'\w{4,}',str)
    
    print('Five letter ',match1)
    print('3, 4, 5 letter ',match2)
    print('at least 4 characters ',match3)

# ismatched27('The quick brown fox jumps over the lazy dog.')


#  28 remove everything except alphanumeric characters from a string
def ismatched28(str):
    
    # match1 = re.findall(r'\w{5}',str)


    # print('SC ',match1)

    str1 = re.compile('[\W_]+')
    print(str1.sub('',str))


# ismatched28('The Quick Brown Fox@$ Jumps$@The Lazy Dog.')

# 29 check a decimal with a precision of 2
def is_decimal(num):
    
    dnumre = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
    result = dnumre.search(num)
    return bool(result)

# print(is_decimal('123.11'))
# print(is_decimal('123.1'))
# print(is_decimal('123'))
# print(is_decimal('0.21'))

# 29  program to remove the parenthesis area in a string

str = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]

def isremoved(str):

    for i in str:
        print(re.sub('\([^)]+\)','',i))

    
# isremoved(str)

# 30 concatenate the consecutive numbers in a given string

def isconcatenate(str):
    
    concat = re.sub(r"(?<=\d)\s(?=\d)", '',str)
    print(concat)
    
# isconcatenate('Enter at 1 20 Kearny Street. The security desk can direct you to floor 1 6. Please have your identification ready.')

# 31 remove lowercase substrings from a given string

def islowersub(str):
    
    concat = re.sub(r"[a-z]", '',str)
    print(concat)

# islowersub('lowercase substrings From a given String')


def capital_words_spaces(str1):
      return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

# print(capital_words_spaces("Python"))
# print(capital_words_spaces("PythonExercises"))
# print(capital_words_spaces("PythonExercisesPracticeSolution"))

#32 convert camel case string to snake case string

def camel_snake_case(str):
    snake = re.sub(r'(\w)([A-Z])',r'\1 \2',str)
    snake_case = re.sub(' ','-',snake).lower()
    print(snake_case)

camel_snake_case('TheNameOfTheRoom')

sft ="B1CD102354"


import re

patt = '[A-z]{2,}\d{3,}'
print(re.search(patt,sft))
'''
B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid
'''
'''
for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')
    '''
print()

u = '4123356789123456'

'''
TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")



try:
    assert re.search(r'^[456]', u)
    assert re.search(r'[0-9]', u)
    assert not re.search(r'[\s_]', u)
    assert not re.search(r'^(\d)\1+$', u)
    assert len(u) == 16
except:
    print('Invalid')
else:
    print('Valid')
'''

s = "> and then she told him she wouldn't settle for less than a Hawaiian pizza, and"
#lookbehind (?<=)
print(re.search(r'(?<![a-z])\d', 'geeksforgeeks14'))

#loohahead (?=)
print(re.search(r'\w(?=[0-9])', 'geeksforgeeks14'))

#lookahead and lookbehind
print(re.search(r'(?<=[a-z])\d(?=[0-9])', 'geeksforgeeks19'))