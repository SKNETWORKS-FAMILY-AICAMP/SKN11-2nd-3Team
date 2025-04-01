import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder


# # members_encoded.csv 파일 로드
# df_members = pd.read_csv('./data/members_encoded.csv')

# # msno와 msno_encoded 컬럼만 추출하여 매핑 만들기
# msno_mapping = dict(zip(df_members['msno'], df_members['msno_encoded']))

# # 대용량 CSV를 분할 처리할 크기 (메모리 16기가면 백만, 32기가면 3백만 까지 여유로움)
# chunk_size = 1_000_000  

# # CSV를 append 모드로 저장하기 위해 처음 파일 생성
# first_chunk = True  

# i = 15
# # for i in range(16,20):
#     # 대용량 CSV 파일을 한 번에 다 읽지 않고 부분적으로 처리
# for chunk in pd.read_csv(f"./data/user_logs_{i}.csv", chunksize=chunk_size):
#     print(chunk.columns)
#     chunk['msno'] = chunk['msno'].map(msno_mapping).astype('Int64')  # msno를 정수형으로 변환
    
#     # 변환된 데이터를 CSV 파일로 저장 (첫 번째 반복에서는 헤더 포함, 이후에는 생략)
#     chunk.to_csv(f"./data/user_logs_encoded{i}", index=False, mode='w' if first_chunk else 'a', header=first_chunk)
        
#     first_chunk = False  # 이후에는 'append' 모드로 저장


# # 판다스에서 실행할려면 파일 크기가 2GB 제한
# chunk_size = 50_000_000  
# file_index = 1  # 파일 번호

# for chunk in pd.read_csv("./data/user_logs_encoded.csv", chunksize=chunk_size):
#     output_file = f"./data/user_logs_encoded_part{file_index}.csv"
#     chunk.to_csv(output_file, index=False)

#     print(f"파일 저장 완료: {output_file}")  # 저장 완료 메시지 출력
#     file_index += 1  # 다음 파일 번호 증가

# print('파일 분할 완료!')


# # 변환할 파일 리스트
# file_list = [f"./data/user_logs_encoded_part{i}.csv" for i in range(1, 9)]

# for file in file_list:
#     # CSV 파일 읽기
#     df = pd.read_csv(file)

#     # msno 컬럼을 Int64로 변환
#     df['msno'] = df['msno'].astype('Int64')

#     # 다시 저장 (덮어쓰기)
#     df.to_csv(file, index=False)

#     print(f"변환 완료: {file}")

# print("모든 파일의 msno를 Int64로 변환 완료!")





# 변환할 파일 리스트
file_list = [f"./data/user_logs_encoded{i}.csv" for i in range(13, 20)]

i=13
for file in file_list:
    # msno별 데이터를 저장할 딕셔너리 (메모리 절약)
    
    aggregated_data = {}
    # CSV 파일 읽기
    df = pd.read_csv(file)
    df = df.drop(columns=['num_unq'],errors='ignore')

    # msno 컬럼을 Int64로 변환
    df['msno'] = df['msno'].astype('Int64')

    # 다시 저장 (덮어쓰기)
    df.to_csv(file, index=False)

    print(f"파일 처리 중: {file}")

    # CSV 파일 읽기 (청크 단위 처리)
    for chunk in pd.read_csv(file, chunksize=3_000_000):  # 청크 크기 조절 가능
        # msno 기준으로 그룹화하여 데이터 합산
        grouped = chunk.groupby("msno").agg(
            num_25=("num_25", "sum"),
            num_50=("num_50", "sum"),
            num_75=("num_75", "sum"),
            num_985=("num_985", "sum"),
            num_100=("num_100", "sum"),
            total_secs=("total_secs", "sum"),
            use_date=("date", "count"),  # 날짜 개수
            start_date=("date", "min"),  # 가장 빠른 날짜
            end_date=("date", "max")  # 가장 마지막 날짜
        ).reset_index()

        # 🏗 기존 데이터와 병합하여 누적 (딕셔너리를 활용한 병합)
        for row in grouped.itertuples(index=False):
            msno = row.msno
            if msno in aggregated_data:
                aggregated_data[msno]["num_25"] += row.num_25
                aggregated_data[msno]["num_50"] += row.num_50
                aggregated_data[msno]["num_75"] += row.num_75
                aggregated_data[msno]["num_985"] += row.num_985
                aggregated_data[msno]["num_100"] += row.num_100
                aggregated_data[msno]["total_secs"] = row.total_secs
                aggregated_data[msno]["use_date"] += row.use_date  # 날짜 개수 누적
                aggregated_data[msno]["start_date"] = min(aggregated_data[msno]["start_date"], row.start_date)
                aggregated_data[msno]["end_date"] = max(aggregated_data[msno]["end_date"], row.end_date)
            else:
                aggregated_data[msno] = {
                    "num_25": row.num_25,
                    "num_50": row.num_50,
                    "num_75": row.num_75,
                    "num_985": row.num_985,
                    "num_100": row.num_100,
                    "total_secs": row.total_secs,
                    "use_date": row.use_date,       # 초기화
                    "start_date": row.start_date,
                    "end_date": row.end_date
                }
    
    # 딕셔너리를 DataFrame으로 변환 (msno를 컬럼으로 유지)
    df_final = pd.DataFrame.from_dict(aggregated_data, orient="index")

    # msno를 일반 컬럼으로 유지하고 인덱스 제거
    df_final.index.name = "msno"
    df_final.reset_index(inplace=True)

    # CSV 파일로 저장 (인덱스 없이)
    df_final.to_csv(f"./data/user_logs{i}.csv", index=False)
    i=i+1

    print(f"변환 완료: {file}")

print("저장 완료")