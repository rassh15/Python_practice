'''
You are given a list which contains some numbers. YOu have to
print a list of next palindromes only if the number
is greater than 10 otherwise you will print the number.

Input: [1, 6, 86, 43]
Output: [1, 6, 88, 44]
'''

def next_number(n):
    
    if palindrome(n):
        #print(f"{n} itself is an palindrome number")
        return n
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
    numb_list = list(map(int, input("Enter element into the list: ").split()))
    palindrome_list = []
    print("List before palindrome\n",numb_list)

    for i in numb_list:
        if i > 10:
            result = next_number(i)
            palindrome_list.append(result)
        else: palindrome_list.append(i)
    
    print('List after palindrome\n',palindrome_list)
    