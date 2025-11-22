import pandas as pd 

data = {
    "Name": ["Ankit", "Akram", "Jhon", "Arya", "Akhil"],
    "Age": [23,24,56,12,10],
    "Salary": [10000,20000,30000,40000,50000],
    "Performance_score": [56,89,30,90,98]
}

df = pd.DataFrame(data)
print(df)

df['Bonus'] = df['Salary'] * 0.1
# df['Total_Salary'] = df['Salary'] + df['Bonus']
df.insert(3,'Total_Salary', df['Salary'] + df['Bonus'])
print(df)
# df.insert(2,'Employee_id', [10,20,30,40,50])
# print(df)
