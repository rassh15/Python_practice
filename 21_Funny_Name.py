'''
Its result day at school and not everyone is happy.
You have decided to make your friends laugh by jumbling
their names to come up with some funny names.

Your program should take the number of names and the names
separated by input, output should be funny names in the same order.


'''

import random

#names = list(input("Enter names seperated by space :  ").split())


names = ['Rashid Ansari','Gopal Das Kumar', 'Tine Agarwal', 'Bawa Bho']
last_name = []

for i in range(len(names)):
    last_name.append(names[i].split(" ", 1)[1])

for i in range(len(names)):
    first_name = names[i].split(" ", 1)[0]
    l_name = last_name[random.randint(0,len(names)-1)]
    print(f"{first_name} {l_name}")