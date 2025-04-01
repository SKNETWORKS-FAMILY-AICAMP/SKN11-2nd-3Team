import pandas as pd

# CSV 파일 불러오기
train_df = pd.read_csv('./data3/train_encoded.csv')
transaction_df = pd.read_csv('./data3/final_merged_member_transaction_data.csv')
user_logs_df = pd.read_csv('./data3/user_logs_encoded_merged_all.csv')

# 세 개의 데이터프레임을 'msno' 기준으로 내부 조인 (inner join)
merged_df = train_df.merge(transaction_df, on='msno', how='inner').merge(user_logs_df, on='msno', how='inner')

# 결과 저장
merged_df.to_csv('realreal_final_data.csv', index=False)

merged_df.info()
