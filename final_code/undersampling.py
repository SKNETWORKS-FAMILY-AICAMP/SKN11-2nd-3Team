import pandas as pd

# 데이터 불러오기
df = pd.read_csv('rrrr_final_data.csv')

# is_churn == 1인 데이터 개수
churn_1_count = df[df['is_churn'] == 1].shape[0]

# is_churn == 0인 데이터 중 1과 3:1 비율을 맞추기 위해 필요한 개수 계산
churn_0_needed_count = churn_1_count * 3

# is_churn == 0인 데이터가 필요한 개수보다 적을 경우 가능한 최대 개수로 샘플링
churn_0_available_count = df[df['is_churn'] == 0].shape[0]
churn_0_needed_count = min(churn_0_needed_count, churn_0_available_count)

# is_churn == 0인 데이터 중 필요한 개수만 샘플링
df_churn_0 = df[df['is_churn'] == 0].sample(n=churn_0_needed_count, random_state=42)

# is_churn == 1인 데이터는 그대로 두고, 두 데이터프레임 합치기
df_balanced = pd.concat([df_churn_0, df[df['is_churn'] == 1]])

# 랜덤하게 섞기
df_balanced = df_balanced.sample(frac=1, random_state=42).reset_index(drop=True)

# 결과 저장
df_balanced.to_csv('undersampling_3_1_data.csv', index=False)

print(f"새로운 데이터셋의 비율:\n{df_balanced['is_churn'].value_counts()}")
