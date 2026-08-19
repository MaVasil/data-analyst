import pandas as pd
# data={
#     "name": ['Alice', 'Bob', 'Charlie', 'David'],
#     "age": [25, 30, 35, 40],
#     "city": ['New York', 'Los Angeles', 'Chicago', 'Houston'],
#     "marks": [85, 90, 95, 80]
# }
# df=pd.DataFrame(data)
# print(df)

# print("Shape of DataFrame:", df.shape)
# print("Columns of DataFrame:", df.columns)
# print("Data types of DataFrame:\n", df.dtypes)
# print("Summary statistics of DataFrame:\n", df.describe())
# print("First 2 rows of DataFrame:\n", df.head(2))
# print("Last 2 rows of DataFrame:\n", df.tail(2))
# print("info of DataFrame:\n", df.info())
# print("Select rows where age is greater than 30:\n")
# print(df[df['age'] > 30])

#handling the missing values example 
example_data = {
    "name": ['Alice', 'Bob', 'Charlie', 'David'],
    "age": [25, 30, None, 40],
    "city": ['New York', 'Los Angeles', 'Chicago', None],
    "marks": [85, 90, 95, None]
}
df_example = pd.DataFrame(example_data)

print("\nDataFrame with missing values:\n", df_example)
print("\nNumber of missing values in each column:\n", df_example.isna().sum())

# df_example.dropna(inplace=True)
# print("\nDataFrame after dropping rows with missing values:\n", df_example)

df_example.fillna({
    'age': df_example['age'].mean(),
    'city': df_example['city'].mode()[0],
    'marks': df_example['marks'].mean()
}, inplace=True)
print("\nDataFrame after filling missing values:\n", df_example)

df_example=df_example.rename(columns={'name': 'Name', 'age': 'Age', 'city': 'City', 'marks': 'Marks'})
print("\nDataFrame after renaming columns:\n", df_example)