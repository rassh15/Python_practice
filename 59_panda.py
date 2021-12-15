#Pandas Library


import pandas as pd
import matplotlib.pyplot as plt

# Basic Pandas
# print(pd.__version__)
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


# dataframee()

def dataframewithfiles():
    
    dfcsv = pd.read_csv('data.csv')

    # print(df) 
    # to check max rows return you can change also by provide value
    # print(pd.options.display.max_rows)

    dfjson = pd.read_json('data.json')

    # print(dfjson.to_string()) 
    data = {
            "Duration":{
                "0":60,
                "1":60,
                "2":60,
                "3":45,
                "4":45,
                "5":60
            },
            "Pulse":{
                "0":110,
                "1":117,
                "2":103,
                "3":109,
                "4":117,
                "5":102
            },
            "Maxpulse":{
                "0":130,
                "1":145,
                "2":135,
                "3":175,
                "4":148,
                "5":127
            },
            "Calories":{
                "0":409,
                "1":479,
                "2":340,
                "3":282,
                "4":406,
                "5":300
            }
            }
    dfdict = pd.DataFrame(data)
    print(dfdict)

    

# dataframewithfiles()

#analyze data frame

def analyzedf():
    df = pd.read_csv('data.csv')
    print(df.head())#show first 5 rows you can specified value also
    print(df.tail())#show last 5 rows you can specified value also
    print(df.info())#information about the data

# analyzedf()

#Cleaning Data

def cleanData():
    df = pd.read_csv('dirtydata.csv')
    print('Before removing rows\n',df)

    # new_df = df.dropna()
    # print('After removing rows\n',new_df)

    # df.dropna(inplace=True)
    
    # df.fillna(130, inplace = True) #130 inserted at all empty cells
    # print('Using Inplace\n',df)

    #only inserting value at empty records for specific column
    '''
    df["Calories"].fillna(130, inplace = True)
    print('Using Column \n',df)
    '''
    # commonly used mean(), median() mode() to replace empty cells
    '''
    x = df["Calories"].mean()

    df["Calories"].fillna(x, inplace = True)
    print('Using mean\n',df)
    '''
    #Correcting date field
    '''
    df['Date'] = pd.to_datetime(df['Date'])
    print(df.to_string())


    df.dropna(subset=['Date'], inplace = True)
    print(df)
    '''

    # wrong data
    #to replace particular cell use loc attribute
    '''
    df.loc[7, 'Duration'] = 45
    print(df)
    '''
    #Now for small data you can do it one by one but large you can set some rules

    #for large data you can set some values in range to fall
    '''
    for x in df['Duration'].index:
        if df.loc[x, 'Duration'] > 120:
            df.loc[x, 'Duration'] = 120
    print(df)
    '''

    #drop rows for wrong data
    '''
    for x in df['Duration'].index:
        if df.loc[x, 'Duration'] > 120:
            df.drop(x, inplace=True)
    print(df)
    '''

    #duplicates 
    '''
    print(df.duplicated()) #return true for duplicated rows
    df.drop_duplicates(inplace=True)#Remove duplicate rows
    print(df.duplicated()) 
    print(df)

    '''
# cleanData()



def correlationdata():


    df = pd.read_csv('data12.csv')
    print(df.corr())

# correlationdata()

def plottingdata():

    df = pd.read_csv('data.csv')
    '''
    df.plot()

    plt.show()'''

    #you can specify type of plot you need like
    '''
    df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')#good correlation
    plt.show()

    df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse') #bad correlation
    plt.show()

    '''

    #Histogram
    #  A histogram needs only one column.
    df["Duration"].plot(kind = 'hist')
    plt.show()



    

plottingdata()

