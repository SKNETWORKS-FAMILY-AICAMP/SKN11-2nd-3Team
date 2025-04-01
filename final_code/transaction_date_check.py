import pandas as pd

# def filter_date(df):      # 20170228~20170331 제외 이상치 제거
#     df = df[df['transaction_date'].between(20170228, 20170331)]
#     df.reset_index(drop=True, inplace=True)
#     return df
# df = pd.read_csv('./origin_data/transactions_v2.csv')

# print(df.info())

# df = filter_date(df)

# print(df.info())

# df.to_csv('filtered_transactions_v2.csv', index=False)

df = pd.read_csv('./origin_data/transactions_v2.csv')

# df.info()
