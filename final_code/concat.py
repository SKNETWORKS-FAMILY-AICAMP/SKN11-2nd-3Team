import pandas as pd

# CSV 파일 불러오기
df1 = pd.read_csv("labeled_transactions.csv")
df2 = pd.read_csv("filter_and_labeled_transactions_v2.csv")

# 병합
merged_df = pd.concat([df1, df2], ignore_index=True)

# 병합된 데이터 저장
merged_df.to_csv("merged_transactions.csv", index=False)


