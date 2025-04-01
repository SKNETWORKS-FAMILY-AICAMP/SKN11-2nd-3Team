import pandas as pd

df = pd.read_csv('./csvfile/realrealreal_final_data.csv')

# bd(나이)가 10살 이상 80살 이하인 데이터만 선택
df = df[df['bd'].between(10, 80, inclusive='both')]
print(df.info())
# df.to_csv('rrrr_final_data.csv', index=False)
