
#We will be creating a calculator program
#With if else or say on terminal only not using any GUI lib

class calculator():

    def add(self, value1, value2):
        return value1+value2
    def mul(self, value1, value2):
        return value1*value2
    def sub(self, value1, value2):
        return value1-value2
    def div(self, value1, value2):
        return value1/value2







cal1 = calculator()

def operations(num):
    first_num = num
    ch = input("1. ADD, 2. SUB, 3. MUL, 4. DIV: 5:Clear 6:Exit: ")

    if ch=='5':
        result = 0
        return result
    elif ch=='6':
        exit()
    second_num = int(input("Enter num: "))

    if ch=='1':
        result = cal1.add(first_num,second_num)
    elif ch=='2':
        result = cal1.sub(first_num,second_num)
    elif ch=='3':
        result = cal1.mul(first_num,second_num)
    elif ch=='4':
        result = cal1.div(first_num,second_num)

    return result


result = 0


while True:

    if result==0:
        first_num = int(input("Enter num: "))
        result = operations(first_num)

    else:
        print(f"Your result for previous operation is {result}")
        print(f"To continue perform operation select")
        
        result = operations(result)

