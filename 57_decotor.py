'''
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator
    

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

print(return_num(5))
'''


def type_check(correct_type):
    print('correct_type ',correct_type)
    def check(old_function):
        print('old_function ',old_function)
        def new_function(arg):
            print('arg ',arg)
            if (isinstance(arg, correct_type)):
                return old_function(arg)
            else:
                print("Bad Type")
        return new_function
    return check
    
                    #times2 = type_check(times2)
# @type_check(int) #time2(num)= type_check()
def times2(num):
    return num*2
# a = 
times2 = type_check(int)(times2)

print(times2(2))
times2('Not A Number')


@type_check(str)
def first_letter(word):
    return word[0]
    

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])



# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()
 
def whisper(text):
    return text.lower()
 
def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print (greeting)
 
greet(shout)
greet(whisper)

def create_adder(x):
    print('x: ',x)
    def adder(y):
        print('y: ',y)
        return x+y
 
    return adder
 
add_15 = create_adder(15)
print(add_15(10))


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()
new()

def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

print('\n')

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner



@smart_divide    #divide = smart_divide(divide)
def divide(a, b):
    print(a/b)

divide(4,5)
print('\n')

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent  #printer = star(percent(printer))
def printer(msg):
    print(msg)


printer("Hello")

print('\n')
'''
def type_check(correct_type):
    print('correct_type ',correct_type)
    def anotherfunc(arg):
        def an(arr):
                
            print('arg ', arg)
            a = isinstance(correct_type, arr)
            if a:
                return True
            else: return 'Bad Type'

        return an

        
        
    return anotherfunc

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])'''