import pandas as pd 

data = {
    "Name": ["Ankit", "Akram", "Jhon", "Arya", "Akhil"],
    "Age": [23,24,56,12,10],
    "Salary": [10000,20000,30000,40000,50000],
    "Performance_score": [56,89,30,90,98]
}

df = pd.DataFrame(data)
# print(df)
# print("Select single column it will return series")
# salary = df["Salary"]
# print(salary)

# Select Multiple columns
subset = df[["Name","Salary"]]
print(subset)

