import numpy as np      # np is the conventional abbreviation for numpy.
import pandas as pd     # pd is the conventional abbreviation for pandas.

#DataFrame:
#
#   It is a data container that can be constructed from a dictionary and lists
#   DataFrame is a dictionary which has lists as it's values
#   
#   Dataframe is a General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column
#

#Making a dataframe using it's constructor
x=pd.DataFrame({"Name":['Mustanseer','Harhsil','Pranit','Arpan','Meet'],
            "Dept":['Comp','Comp','Comp','IT','Comp'],
            "Years of experience":[2,'9000+',7,7,100]})
print(x)

#Importing data from csv file into a DataFrame variable
y=pd.read_csv("CSVDemo.csv")
print(y)

#printing only the first 5 rows
print(y.head())

n=10

#printing the first n columns
print(y.head(n))

#printing only the last 5 rows
print(y.tail())

#printing the last n rows
print(y.tail(n))

## Accessing data in dataframe:

#printing the column names:
print(y["Runs"])
print(y["Number"])

#printing 2nd row
print(y.loc[2,:])

#printing from 2nd row to 5th row
print(y.loc[2:5,:])

#printing the data on 5th row in Runs column
print(y.loc[5,"Runs"])

#For the Basics, This should be enough. We'll see other functionalities of pandas as we encounter them