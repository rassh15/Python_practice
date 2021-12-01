'''
The Next Palindrome
A palindrome is a string which peversed is equal to itself:
Example: 616, MOM, 676, 100001

You have to take a number as an input from the user.
You have to find the next palindrome corresponding to 
that number.
Your input should be number of test cases and then
take all the cases as input from the user.
Input:
first input will number of test case you want
ex: 3
so next input will be three inputs of numbers to find
the next number palindrome.

'''


def next_number(n):

    if palindrome(n):
        print(f"{n} itself is an palindrome number")
        return True
    else:
        while True:
            n = n + 1
            output = palindrome(n)
            if output: return n

def palindrome(n1):
    org_numb = n1
    rev_digit = ''

    while n1>0:   
        
        tmp1 = n1%10
        n1 = n1//10

        rev_digit = rev_digit + str(tmp1)

        
    if org_numb == int(rev_digit):
        return True
    else: return False




    
if __name__ == '__main__':
    num_of_test = int(input("Enter the number of test cases you want to test: "))
    num_to_test = list(map(int, input(f"Enter {num_of_test} numbers seperated by space").split()))



    for i in num_to_test:
        result = next_number(i)
        if result:
            print(f"{result} is the palindrome number after {i}")
