import pandas as pd

df = pd.read_csv('members_encoded2.csv')
df.info()
df.drop(columns=['gender'],inplace=True)


df.to_csv('final_members.csv')