import pandas as pd

# df=pd.DataFrame({
#     "name": ['Alice', 'Bob', 'Charlie', 'David'],
#     "age": [25, 30, 35, 40],
#     "city": ['New York', 'Los Angeles', 'Chicago', 'Houston'],
#     "marks": [85, 90, 95, 80]
# })

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)

# df_sales=pd.DataFrame({
#     "order_id": [1, 2, 3, 4],
#     "product": ['A', 'B', 'C', 'D'],
#     "quantity": [10, 20, 30, 40],
#     "price": [100, 200, 300, 400]
# })

# df_users=pd.DataFrame({
#     "user_id": [1, 2, 3, 4],
#     "name": ['Alice', 'Bob', 'Charlie', 'David'],
#     "email": ['mdvasil07@gmail.com', 'johndoe@gmail.com', 'janesmith@gmail.com', 'mikejohnson@gmail.com']
# })


# with pd.ExcelWriter("report.xlsx") as writer:
#     df_sales.to_excel(writer, sheet_name="Sales", index=False)
#     df_users.to_excel(writer, sheet_name="Users", index=False)

#appending user data into the report.xlsx file
df_new_users=pd.DataFrame({
    "user_id": [5, 6],
    "name": ['Eve', 'Frank'],
    "email": ['raju@gmail.com', 'rani@gmail.com']
})

#i want this into the sheet name "Users" in the report.xlsx file, so i will use mode='a' and header=False to avoid writing the header again
with pd.ExcelWriter(
    "report.xlsx",
    mode="a",
    engine="openpyxl",
    if_sheet_exists="overlay"
) as writer:
    df_new_users.to_excel(
        writer,
        sheet_name="Users",
        index=False,
        header=False,
        startrow=writer.book["Users"].max_row
    )

    print("New users appended to the 'Users' sheet in report.xlsx")
    print(writer.book["Users"])  # Print the maximum row number in the "Users" sheet