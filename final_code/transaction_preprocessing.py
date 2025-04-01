import pandas as pd

# # 데이터 로드
# df = pd.read_csv("merged_transactions.csv")
# print(df.info())
# # plan_list_price보다 actual_amount_paid가 큰 데이터 제거
# df = df[df["plan_list_price"] >= df["actual_amount_paid"]]

# # payment_plan_id 컬럼 제거 
# df.drop(columns=["payment_method_id"], inplace=True, errors='ignore')

# # 그룹화하여 필요한 컬럼 계산
# agg_df = df.groupby("msno_encoded").agg(
#     transaction_count=("msno_encoded", "count"),
#     is_cancel_sum=("is_cancel", "sum"),
#     is_cancel_mean=("is_cancel", "mean"),
#     actual_amount_paid_sum=("actual_amount_paid", "sum"),
#     is_auto_renew_mean=("is_auto_renew", "mean"),
#     membership_expire_date_max=("membership_expire_date", "max"),
# ).reset_index()


# # is_cancel == 0인 데이터만 필터링하여 plan_days_sum 계산
# plan_days_sum = df[df["is_cancel"] == 0].groupby("msno_encoded")["payment_plan_days"].sum()

# # 결과 병합 (NaN 값은 0으로 대체)
# agg_df["plan_days_sum"] = agg_df["msno_encoded"].map(plan_days_sum).fillna(0)

# print(agg_df.info())

# # 결과 저장
# agg_df.to_csv("processed_transactions.csv", index=False)

# df = pd.read_csv('processed_transactions.csv')
# df = df[df["actual_amount_paid_sum"] > 0]
# df.to_csv('processed_transaction.csv',index=False)
# print(df.info())

df = pd.read_csv('processed_transaction.csv')

# msno를 정수형(int)으로 변환
df['msno'] = df['msno_encoded'].astype(int)
df.drop(columns=['msno_encoded'], inplace=True)
# CSV 파일로 저장 (인덱스 제거)
df.to_csv('transaction_final_data.csv', index=False)