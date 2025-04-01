import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# 데이터 불러오기
df = pd.read_csv('realrealreal_final_data.csv')

# 타겟 및 불필요한 컬럼 제거
X = df.drop(columns=['is_churn', 'msno', 'start_date', 'end_date'])
y = df['is_churn']

# 피처 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 데이터프레임 변환 (상관관계 분석을 위해)
X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns)

# 피어슨 상관계수 계산
corr_matrix = X_scaled_df.corr(method='pearson')

# 상관관계 히트맵 출력
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", linewidths=0.5)
plt.title("Feature Pearson Correlation Heatmap")
plt.show()

# 상관관계 데이터 반환
corr_matrix
