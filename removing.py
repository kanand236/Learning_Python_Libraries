import pandas as pd 

data = {
    "Name": ["Ankit", "Akram", "Jhon", "Arya", "Akhil"],
    "Age": [23,24,56,12,10],
    "Salary": [10000,20000,30000,40000,50000],
    "Performance_score": [56,89,30,90,98]
}

df = pd.DataFrame(data)
print(df)

df.drop(columns=['Performance_score', 'Age'], inplace=True)
print(df)