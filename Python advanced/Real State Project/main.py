# we are solving the exploratory data analytics problem .
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('real-estate.csv')
# print(df.head())
# print(df.shape)
# print(df.info())

df=df.drop_duplicates()
df.columns=df.columns.str.strip().str.lower().str.replace(' ', '_')

df['price']=df['price'].astype(str).str.replace('$','').str.replace(',','').astype(int)
df['area']=df['area'].astype(str).str.replace(' ', '').astype(int)
df['rate_per_sqft']=df['rate_per_sqft'].astype(str).str.replace(',','').astype(int)

df['status']=df['status'].str.strip().str.lower()
df['rera_approval']=df['rera_approval'].str.strip().str.lower()
df['flat_type']=df['flat_type'].str.strip().str.lower()

# print(df.info())

# 1. Which is the costliest flat in the dataset?
# max_idx=df['price'].idxmax()
# costliest_flat=df.loc[max_idx]

# print("Costliest Flat Details:")
# print(costliest_flat)


# 2. Which locality has the highest average price?
# highest_avg_price_locality = df.groupby('locality')['price'].mean().sort_values(ascending=False).head(1)
# print("Locality with Highest Average Price:")
# print(highest_avg_price_locality)

# 3. Which locality has the highest rate per square foot?
# highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False).head(1)
# print("Locality with Highest Rate per Square Foot:")
# print(highest_rate_locality)

# 4. Do ready-to-move properties cost more than under-construction properties?
# dat=df.groupby('status')['price'].mean()
# print("Average Price by Property Status:")
# print(dat)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
# print(dat)

# data_cr=dat/1e7
# print("Average Price by Property Status (in Crores):")
# print(data_cr)
# sns.barplot(x=dat.index, y=dat.values)
# #display it 
# plt.show()
# sns.barplot(x=dat.index, y=dat.values,hue='status',data=dat)

# 5. Do RERA-approved properties command a price premium?
# premium = df.groupby('rera_approval')['price'].mean()
# sns.barplot(x=premium.index, y=premium.values)
# plt.title('Average Price by RERA Approval Status')
# plt.xlabel('RERA Approval Status')
# plt.ylabel('Average Price')
# plt.show()

# 6. How does area (sqft) impact property price?
# sns.scatterplot(x='area', y='price', data=df)
# plt.title('Property Price vs Area')
# plt.show()

# 7. Which BHK configuration is the most expensive on average?
# df.groupby('bhk_count')['price'].mean().sort_values(ascending=False).plot(kind='bar')
# plt.title('Average Price by BHK Configuration') 
# plt.xlabel('BHK Configuration')
# plt.ylabel('Average Price')
# plt.show()

# 8. Which property type (Apartment, Floor, Plot) is the costliest?
# property_type_avg_price = df.groupby('property_type')['price'].mean().sort_values(ascending=False).head(1)
# print("Costliest Property Type:")
# print(property_type_avg_price)

# 9. Do certain builders or companies consistently price higher?
# df.groupby('company_name')['price'].mean().sort_values(ascending=False).head(10).plot(kind='bar')
# plt.title('Average Price by Company')
# plt.xlabel('Company Name')
# plt.ylabel('Average Price')
# plt.show()

# 10. Are larger homes always more expensive per square foot?
# sns.scatterplot(x='area', y='rate_per_sqft', data=df)
# plt.title('Rate per Square Foot vs Area')
# plt.xlabel('Area')
# plt.ylabel('Rate per Square Foot')
# plt.show()
