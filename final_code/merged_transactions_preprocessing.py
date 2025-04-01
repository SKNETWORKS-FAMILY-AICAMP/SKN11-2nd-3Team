import pandas as pd


df = pd.read_csv('merged_transactions.csv')

df = df[df['transaction_date']<=df['membership_expire_date']]
df.info()
df.to_csv('final_merged_transactions.csv')