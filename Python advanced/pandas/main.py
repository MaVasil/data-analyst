import pandas as pd 

df = pd.read_csv('data.csv', skiprows=2, usecols=['order_id', 'order_status', 'city'], index_col='order_id')
# print(df.info())
# print(df)

# # Select all Delivered orders from Bangalore
# delivered_orders = df[(df['order_status'] == 'Delivered') & (df['city'] == 'Bangalore')]
# print(delivered_orders)

df2 = pd.read_excel("Random Data Generator.xlsx", sheet_name='Sheet1' )
print(df2)
print(pd.ExcelFile("Random Data Generator.xlsx").sheet_names)