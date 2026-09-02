import pandas as pd

df = pd.read_csv("Workbook1.csv")

target = "ammar"

# Returns True if 'Alice' exists in ANY column
exists = (df == target).any().any()
print(exists)
print(df)
# i=int(input("enter ID: "))
# row_m=df[df["ID"]==i]
# print(row_m)
df["purpose"]="class"
df.loc[2,"purpose"]="registration"
df.dropna(inplace=True)
df=df[df["ID"]!=324232]
print(df)
print(df.mean(numeric_only=True))

