import pandas as pd

df=pd.DataFrame({
    "name": ['Alice', 'Bob', 'Charlie', 'David'],
    "age": [25, 30, 35, 40],
    "city": ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    "marks": [85, 90, 95, 80]
})

df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)

df_sales=pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "product": ['A', 'B', 'C', 'D'],
    "quantity": [10, 20, 30, 40],
    "price": [100, 200, 300, 400]
})

df_users=pd.DataFrame({
    "user_id": [1, 2, 3, 4],
    "name": ['Alice', 'Bob', 'Charlie', 'David'],
    "email": ['mdvasil07@gmail.com', 'johndoe@gmail.com', 'janesmith@gmail.com', 'mikejohnson@gmail.com']
})


with pd.ExcelWriter("report.xlsx") as writer:
    df_sales.to_excel(writer, sheet_name="Sales", index=False)
    df_users.to_excel(writer, sheet_name="Users", index=False)