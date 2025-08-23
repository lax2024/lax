import pandas as pd

# Series() - one dimensional labeled array

s = pd.Series([10,20,30,40])
print(s)

# DataFrame() - two dimensional labeled data structure

data = {"Name":["Alice","Bob","Kayla","Raya","Paedyn","Maya"],"Age":[25,27,20,23,26,None],"City":["Calicut","Kannur","Gavi","LA","WC","Jamaica"]}
df = pd.DataFrame(data,index = ["a","b","c","d","e","f"])
print(df)

# head() used to return first N rows of a DataFrame

print(df.head()) #returns first 5 rows
print(df.head(3))

# tail() oppodite of head

print(df.tail()) #returns last 5 rows
print(df.tail(2))

# info()

df.info()

# describe()

print(df.describe())

# columns() returns labels of columns

print(df.columns)

# shape returns a tuple representing dimensionality of DataFrame

print(df.shape)

# loc[] access a group of rows and columns by their labels or boolean arrays

print(df.loc["a"])
print(df.loc["b","Name"])
print(df.loc[:,["Name","Age"]])

# iloc[] access rows and columns by integer position

print(df.iloc[0])
print(df.iloc[1,0])
print(df.iloc[:,0:2])

# isnull() used to detect null values

print(df.isnull())

# dropna() removes rows or columns that contain null value

# print(df.dropna())

# fillna() replaces null value with specified value

print(df.fillna(0))
df["Age"].fillna(df["Age"].mean(),inplace = True)
print(df)

