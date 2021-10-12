'''
Faulty calculator
Design a calculator which will correctly solve all the problems except the 
following ones:
45*3 = 555,  56 + 9 = 77, 56/6 = 4
Take operator and two digit inputs and return the result
'''
def calc(first, second, operation):

    if operation in number_list:
        if int(first) in number_list:
            if int(second) in number_list:
                if operation == '*':
                    return 555
                elif operation == '+':
                    return 77
                elif operation == '/':
                    return 4    


    elif operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second
    elif operation == '%':
        return first % second


number_list = [45, 56, 3, 9, 6, '*', '+', '/']

first_numb, second_numb, operatorr =input("Enter the two number and operator: ").split()


print(f"Result is {calc(int(first_numb), int(second_numb), operatorr)}")

