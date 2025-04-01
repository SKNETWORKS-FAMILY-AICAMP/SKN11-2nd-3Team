import pandas as pd

df1 = pd.read_csv('train_v2_final_201702.csv')
df2 = pd.read_csv('./csvfile/realrealreal_final_data.csv')


# msno 기준으로 내부 조인 (df1에 있는 msno가 df2에 없으면 제거)
merged_df = df1.merge(df2, on='msno', how='inner', suffixes=('_df1', '_df2'))

# 'is_churn' 칼럼이 두 데이터프레임에 공통으로 있는데, df1의 'is_churn' 값을 사용
merged_df['is_churn'] = merged_df['is_churn_df1']
merged_df.drop(columns=['is_churn_df1', 'is_churn_df2'], inplace=True)

# 결과 저장
merged_df.to_csv('new_data.csv', index=False)

print(merged_df.info())

