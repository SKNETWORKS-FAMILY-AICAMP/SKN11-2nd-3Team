# final_members.csv 파일과 final_processed_transactions.csv 파일을 msno를 기준으로 결합

import pandas as pd

df1 = pd.read_csv('final_members.csv')
df2 = pd.read_csv('final_processed_transactions.csv')

# 2개의 데이터프레임을 'msno' 기준으로 내부 조인 (inner join)
merged_df = df1.merge(df2, on='msno', how='inner')
# 결과 저장
merged_df.to_csv('merged_member_transaction_data.csv', index=False)
