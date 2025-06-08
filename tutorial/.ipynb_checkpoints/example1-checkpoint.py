import pandas as pd

df = pd.DataFrame(
    {'A':[1,2,3]},
    
    )
df1 = pd.DataFrame(
    [
        {'a':1,'b':2,'c':3},
        {'a':4,'b':5,'c':6}
    ]
)

# print(df)
# print(df1)

# extract column
# df2 = pd.DataFrame(df1['a'])
# print(df2)


excel_data = pd.read_excel(r"C:\Users\WYTM\Desktop\RIG Intern\20250608\Pandas-RIG-Learn\tutorial\abc.xlsx")

print(excel_data)

df3 = pd.DataFrame(excel_data[['First Name','Last Name','Dept']])
print(df3)

print(df3.head())
print(df3.tail())

print(df3.info())

print(df3.describe())