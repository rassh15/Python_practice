nums = [i for i in range(1,1001)]
string = "Practice Problems to Drill List Comprehension in Your Head."

# Find all of the numbers from 1–1000 that are divisible by 8

# print([x for x in nums if x%8==0])

# Find all of the numbers from 1–1000 that have a 6 in them

# print([x for x in nums if str(6) in str(x)])

# Count the number of spaces in a string (use string above)
# print(string.count(" "))
# print(len([x for x in string if x==' ']))

# Remove all of the vowels in a string (use string above)

# print(''.join([x for x in string if x.lower() not in ['a','e','i','o','u',]]))

# Find all of the words in a string that are less than 5 letters (use string above)

# print([x for x in string.split(' ') if len(x)<5])

# Use a dictionary comprehension to count the length of each word in a sentence (use string above)

# print({x:len(x) for x in string.split(' ')})

# Use a nested list comprehension to find all of the numbers 
# from 1–1000 that are divisible by any single digit besides 1 (2–9)

# print([[x for x in nums if x%y==0] for y in range(2,10)])
# q7_answer = [num for num in nums if True in [True for divisor in range(2,10) if num % divisor == 0]]
# print(q7_answer)

# print{num:max([divisor for divisor in range(1,10) if num % divisor == 0]) for num in nums}

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

#Type your answer here.

lst={a.upper():b for a,b in dict.items() if b<5000}

print(lst)






