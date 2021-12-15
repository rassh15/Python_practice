#Pandas Library

# Basic Pandas
# print(pd.__version__)

import pandas as pd
def basic():
    mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
    }

    df = pd.DataFrame(mydataset)

    print(df)

# basic()

#series

def seriess():
    myseries = [41,52,53,64,85]

    myvar = pd.Series(myseries)
    #YOu can provide your own label
    myvarwithlable = pd.Series(myseries, index=['x','y','z','a','b'])
    print('Without Lables\n',myvar)
    print(myvar[1]) #can access series value like this also
    print('With Labels\n',myvarwithlable)

    #another form of series data (keys becomes index of table)
    runs = {"day1": 420, "day2": 380, "day3": 390}
    myrun = pd.Series(runs)
    print(myrun)
    # You can also limit data by using keys
    myrunlimitkey = pd.Series(runs,index=['day1','day3'])
    print(myrunlimitkey)

# seriess()

def dataframee():
    data = {
    "Run": [340, 200, 300],
    "Over": [50, 40, 45]
    }

    df= pd.DataFrame(data)

    print(df)

    # andas use the loc attribute to return one or more specified row(s)
    print(df.loc[0])
    #use a list of indexes:
    print(df.loc[[0, 1]])

    # [] use of this represent dataframe
    #you can also provide indexes same as series using index arg in dataframe

    df2 = pd.DataFrame(data,index=['Match1','Match2','Match3'])
    print(df2)

    #you can use index in loc attribute to access data

    print(df2.loc['Match3'])


dataframee()
