import pandas as pd
# registration_init_time > transaction_date_max 인 데이터 제거 
df = pd.read_csv('merged_member_transaction_data.csv')

df.drop(columns=['Unnamed: 0'],inplace = True)
print(df.info())

df = df[df['registration_init_time']<=df['transaction_date_max']]
print(df.info())

df.to_csv('final_merged_member_transaction_data.csv')

