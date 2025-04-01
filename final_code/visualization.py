import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('rrrr_final_data.csv')

plt.figure(figsize=(8, 6))
sns.histplot(data=df, x='is_auto_renew_mean', hue='is_churn', multiple='stack', kde=True)
plt.title("is_auto_renew_mean vs is_churn")
plt.xlabel("is_auto_renew_mean=")
plt.ylabel("Frequency")
plt.show()
