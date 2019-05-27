import pandas as pd

#df_xls = pd.read_excel("Projet_Data.xlsx")
#print(df_xlsx.head(2))

df=pd.read_excel("Projet_Data.xlsx")
#print(df.colums)

a=df.loc[df['Moyenne']>=10]
print(a)

a.to_csv('modified.csv' ,index=False)

b=df.loc[df['Age']>=20]
print(b)

b.to_csv('modified.csv' ,index=False)
