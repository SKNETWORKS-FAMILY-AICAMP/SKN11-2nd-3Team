import pandas as pd

df = pd.read_csv('rrrr_final_data.csv')

print(df['is_churn'].value_counts())