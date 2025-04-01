import pandas as pd

# df = pd.read_csv('./data/user_logs_encoded_merged_all_0_to_5.csv')

# # 'msno' 컬럼에서 중복된 값의 빈도를 계산
# duplicate_counts = df['msno'].value_counts()

# # 중복된 값들만 필터링 (빈도가 1보다 큰 값들만)
# duplicates = duplicate_counts[duplicate_counts > 1]

# print("중복된 msno 값과 빈도수:")
# print(duplicates)

# print(len(duplicates))  # 중복된 msno 값의 개수 (고유한 중복값 개수)
# print(duplicates.sum()) # 중복된 msno 값들의 총 빈도수 (중복 포함 개수)


# import pandas as pd

# # CSV 파일 읽기
# df = pd.read_csv('./data/user_logs_encoded_merged_all.csv')

# # msno를 제외한 컬럼 선택
# columns_to_check = df.columns.difference(['msno'])

# # 나머지 컬럼 값이 모두 0인 행을 제외
# filtered_df = df[~(df[columns_to_check] == 0).all(axis=1)]

# # 남아 있는 msno의 개수 출력 (고유한 값의 개수)
# print(f"조건을 만족하는 msno 개수: {filtered_df['msno'].nunique()}")


df= pd.read_csv('processed_transaction.csv')
duplicate_counts = df['msno_encoded'].value_counts()
# 중복된 값들만 필터링 (빈도가 1보다 큰 값들만)
duplicates = duplicate_counts[duplicate_counts > 1]

print("중복된 msno 값과 빈도수:")
print(len(duplicates))