import pandas as pd

# 데이터 로드
df = pd.read_csv('./csvfile/realrealreal_final_data.csv')

# 'is_churn' 컬럼 값별 샘플 수 확인
class_counts = df['is_churn'].value_counts()
min_count = class_counts.min()  # 적은 클래스의 샘플 수에 맞춤
print(class_counts)
# # 각 클래스에서 동일한 개수로 샘플링
# df_0 = df[df['is_churn'] == 0].sample(n=min_count, random_state=42)
# df_1 = df[df['is_churn'] == 1].sample(n=min_count, random_state=42)

# # 언더샘플링된 데이터프레임 생성
# df_balanced = pd.concat([df_0, df_1]).sample(frac=1, random_state=42)  # 섞기

# # 결과 저장
# df_balanced.to_csv('rrr_balanced.csv', index=False)

# print("언더샘플링 완료: 'rrr_balanced.csv' 저장됨")
