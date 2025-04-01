import pandas as pd

def labelmapping(df):
    # df에 members_df의 숫자값을 매핑 (msno 기준, left join 사용해서 members_df에 없는 msno 값은 NaN) 
    df = df.merge(members_df, on='msno', how='left')

    # 'msno_encoded'가 NaN인 행 삭제
    df = df.dropna(subset=['msno_encoded'])

    # 기존 msno 컬럼 삭제 
    df.drop(columns=['msno'], inplace=True)

    return df 

# msno, label인코딩 된 msno값 불러오기
members_df = pd.read_csv('./data/members_encoded.csv')

# 변환하려는 df 불러오기 (필요할 때마다 파일명만 수정해서 사용)
df = pd.read_csv('./origin_data/train_v2.csv')
print(df.info())
df = labelmapping(df)
print(df.info())

# 저장
df.to_csv('labeled_train_v2.csv', index=False)