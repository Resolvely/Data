import pandas as pd


print("merging begin!")
df1 = pd.read_csv('013 effy2022.csv')
df2 = pd.read_csv('021 adm2022.csv')
df3 = pd.read_csv('065 s 2022_nh.csv')
df4 = pd.read_csv('069 eap2022.csv')
df5 = pd.read_csv('081 sfa2122.csv')
df6 = pd.read_csv('091 gr2022_pell_ssl.csv')

merged_df = pd.merge(df1, df2, on='UNITID', how='outer')
merged_df = pd.merge(merged_df, df3, on='UNITID', how='outer')
merged_df = pd.merge(merged_df, df4, on='UNITID', how='outer')


print("merging done!")
print(merged_df)