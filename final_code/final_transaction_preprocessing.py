import pandas as pd

# 데이터 로드
file_path = 'final_merged_transactions.csv'
df = pd.read_csv(file_path)

# msno를 정수형(int)으로 변환
df['msno'] = df['msno_encoded'].astype(int)
df.drop(columns=['msno_encoded'], inplace=True)

# plan_list_price 보다 actual_amount_paid 가 큰 데이터 제거
df = df[df['actual_amount_paid'] <= df['plan_list_price']]

# payment_method_id 컬럼 제거
df.drop(columns=['payment_method_id'], inplace=True)

# msno_encoded 기준 그룹화
grouped_df = df.groupby('msno').agg(
    transaction_date_max=('transaction_date', 'max'),  # 0) transaction_date 중 max 값
    transaction_count=('msno', 'count'),  # 1) 거래 횟수
    is_cancel_sum=('is_cancel', 'sum'),  # 2) is_cancel 수 합계
    is_cancel_mean=('is_cancel', 'mean'),  # 3) is_cancel 평균
    actual_amount_paid_sum=('actual_amount_paid', 'sum'),  # 4) actual_amount_paid 총합
    is_auto_renew_mean=('is_auto_renew', 'mean'),  # 5) is_auto_renew 평균
    payment_plan_days_sum=('payment_plan_days', lambda x: x[df.loc[x.index, 'is_cancel'] == 0].sum())  # 6) is_cancel == 0인 경우만 합산
).reset_index()

# actual_amount_paid_sum이 0 초과인 데이터만 필터링
filtered_df = grouped_df[grouped_df['actual_amount_paid_sum'] > 0]

# 결과 저장
filtered_df.to_csv('final_processed_transactions.csv', index=False)

print(filtered_df.info())