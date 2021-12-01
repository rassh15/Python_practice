'''
Problem
Take age or year of birth as an input from the user and 
tell them when they will turn 100 years old.
Don't use any type of module like datetime or dateutils.
They can optionally provide a year and your program
must tell their age in that particular year

Handle all sorts of error like:
- You are not yet born
- You seen to be the oldest person alive
- You can also handle any othererror if possible

'''
curr_year = 2021
print("To know in which year you will turn 100 year old")
age_year = int(input("Enter age or year of birth: "))
year_100 = 0
birth_year = 0
curr_age = 0
if age_year>200:
    if age_year>2021:
        print("Error! Please enter correct year ")
    else:
        birth_year = age_year
        curr_age = curr_year - birth_year
        year_100 = age_year + 100
        print(f"You will be 100 year old in year {year_100}")

else:
    birth_year = curr_year - age_year
    curr_age = curr_year - birth_year
    tmp = curr_year + (100 - age_year)
    print(f"You will be 100 year old in year {tmp}")

ch = input("Enter year to know age in that year or else No")
tmp = int(ch) - curr_year
print(f"You will {curr_age + tmp } old in year {int(ch)}") if ch!="No" else print("Done")




