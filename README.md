# 🎵 KKBox(대만 음악 스트리밍 서비스) 사용자 이탈 예측 프로젝트
## 3 Team
<table>
  <thead>
    <td align="center">
      <a href="">
        <img src="" width="150" alt="jangsoo"/><br /><hr/>
        김장수
      </a><br />
    </td>
    <td align="center">
      <a href="">
        <img src="" width="150" alt="Sungil"/><br /><hr/>
        방성일
      </a><br />
    </td>
    <td align="center">
      <a href="">
        <img src="https://github.com/user-attachments/assets/a28f14f0-2e04-4bb9-be4f-2fe81924e523" height="150" width="150" alt="jungsoo"/><br /><hr/>
        배정수
      </a><br />
    </td>
    <td align="center">
      <a href="">
        <img src="" width="150" alt="hyundae"/><br /><hr/>
        이현대
      </a><br />
    </td>
      <td align="center">
      <a href="https://github.com/minjung2266">
        <img src="https://github.com/minjung2266.png" width="150" alt="minjeong"/><br /><hr/>
        이민정
      </a><br />
    </td>
  </thead>
</table>

---
# 📅 개발 기간
**2025.03.31 ~ 2025.04.01 (총 2일)**

##  🎯 프로젝트 개요

### **프로젝트 목표**
- KKBox(대만 음악 스트리밍 서비스) 사용자의 **이탈 여부(is_churn)** 를 예측하는 모델을 개발하여, KKBox 사용자의 이탈 방지를 효과적으로 수행하여 수익 향상에 기여함을 목적으로 함.

### **기대효과**:

 1. **수익 손실 방지**  
   신규 고객 확보 비용은 기존 고객을 유지하는 비용보다 높음. 따라서 기존 고객의 이탈을 줄이는 것이 비용적인 면에서 효율적.

2. **고객 충성도 향상**  
   고객 이탈 가능성이 높은 고객을 조기에 식별하여 맞춤형 유지 전략을 제공 -> 고객 충성도를 높여 장기적으로 더 높은 매출 창출이 가능

3. **비즈니스 프로세스 개선**  
   고객 이탈 데이터를 분석하여 제품, 서비스, 또는 마케팅 전략에서 개선이 필요한 부분을 파악 가능.

4. **마케팅 리소스 최적화**  
   이탈 가능성이 높은 고객에 집중하여 고객 유지 차원에서 마케팅 자원을 효율적으로 배분 가능. 이는 기업의 ROI(투자 대비 효과) 향상으로 연결됨.


### **접근 방식**:
  - 데이터를 목적에 맞게 전처리를 진행하고 여러 모델 중 학습 후 성능이 좋은 모델을 바탕으로, 이탈 여부에 큰 영향을 미치는 feature들을 시각화(그래프 등)를 통해 확인함. 이를 통해 KKBox에 제공할 수 있는 인사이트를 도출
   
### **타겟 변수**: **`is_churn(이탈여부)`** ('1': 이탈 o , '0': 퇴사 x) (이탈 기준 : 현재 멤버십이 만료된 후 30일 이내에 새로운 유효한 서비스 구독이 없는 것)


## 📂데이터 구성
### - 데이터소스: [WSDM - KKBox의 Churn Prediction Challenge](https://www.kaggle.com/c/kkbox-churn-prediction-challenge/overview)
#### [ DataSet : 전처리 전]

1. members_v3.csv (유저 테이블)
    - **설명**: 유저의 프로필 정보
    - **컬럼**
        - `msno`: 유저 ID
        - `city`: 도시
        - `bd`: 나이 
        - `gender`: 성별
        - `registered_via`: 가입 경로
        - `registration_init_time`: 가입 날짜 (`%Y%m%d`)
2. train_v2.csv / train1.csv
    - **설명**: 유저 ID와 이탈 여부(`is_churn`)가 포함된 학습용 데이터셋 (2017년 2월까지의 데이터 기반)
    - **컬럼**
        - `msno`: 유저 ID
        - `is_churn`: 이탈 여부 ('1' = 이탈 o, '0' = 이탈 x)
3.  transactions.csv / transactions_v2.csv 
    - **설명**: 유저의 **결제 이력**이 담긴 데이터셋
    - **컬럼**
        - `msno`: 유저 ID
        - `payment_method_id`: 결제 방식 ID x
        - `payment_plan_days`: 플랜 기간 (일 기준)   sum
        - `plan_list_price`: 플랜 정가 (NTD)  mean/sum
        - `actual_amount_paid`: 실제 결제 금액 (NTD). mean/sum
        - discount_amout : 할인율 1 - (actual_amount_pain / plan_list_price).  mean/sum
        - `is_auto_renew`: 자동 갱신 여부
        - `transaction_date`: 결제 날짜 (`%Y%m%d`)
        - `membership_expire_date`: 회원 만료일 (`%Y%m%d`)
        - `is_cancel`: 구독 취소 여부

4.  user_logs.csv / user_logs_v2.csv


#### [ DataSet : 최종 데이터]
| 컬럼명                   | 설명 (예상)                                                                 |
|------------------------|---------------------------------------------------------------------------|
| `msno`                 | 사용자 고유 ID                                                              |
| `is_churn`             | 이탈 여부 (1: 이탈, 0: 유지)                                                 |
| `city`                 | 사용자의 도시 (지역 정보)                                                    |
| `bd`                   | 사용자의 나이 (birth date에서 유추)                                          |
| `registered_via`       | 등록 경로 (앱, 웹, 페이스북 등)                                              |
| `registration_init_time` | 가입한 날짜 (YYYYMMDD 형식)                                                |
| `transaction_date_max` | 가장 최근 거래 날짜                                                          |
| `transaction_count`    | 총 거래 횟수                                                                 |
| `is_cancel_sum`        | 취소된 거래 횟수 총합                                                         |
| `is_cancel_mean`       | 평균적으로 거래가 취소된 비율                                                 |
| `actual_amount_paid_sum` | 실제 결제된 금액 총합                                                       |
| `is_auto_renew_mean`   | 자동 갱신 여부 평균 (1: 자동 갱신됨, 0: 아님)                                 |
| `payment_plan_days_sum` | 전체 결제 플랜 일수 합                                                       |
| `start_date`           | 마지막 구독 시작일                                                           |
| `end_date`             | 마지막 구독 종료일                                                           |
| `num_25`               | 25% 정도 감상한 곡 수                                                         |
| `num_50`               | 50% 정도 감상한 곡 수                                                         |
| `num_75`               | 75% 정도 감상한 곡 수                                                         |
| `num_985`              | 거의 끝까지 (98.5%) 감상한 곡 수                                              |
| `num_100`              | 100% 감상한 곡 수                                                             |
| `total_secs`           | 전체 감상 시간(초 단위)                                                       |
| `use_date`             | 해당 사용자의 데이터가 몇 개의 날짜에 걸쳐 있는지 (사용일 수)                 |

### TechSet
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
  <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=vscode&logoColor=white">
  <img src="https://img.shields.io/badge/numpy-%235865F2.svg?style=for-the-badge&logo=numpy&logoColor=white">
</p>
<p align="center">
  <img src="https://img.shields.io/badge/pandas-%23000000.svg?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
</p>
<br/><br/>

### EDA
#### 1. 데이터 전처리<br/>
![Image](https://github.com/user-attachments/assets/fe0b94b1-b6eb-49e7-aa27-33c52aac836d)
#### transaction_v2.csv 에 대한 전처리 내용
- transaction_date_check.py
  
캐글의 데이터 설명에 명시된 내용을 보면 transaction.csv 파일은 2017년 02월 28일 까지의 거래 기록, transaction_v2.csv 파일은 그 이후로 2017년 03월 31일 까지의 거래 기록으로 확인된다.<br/>
하지만 transaction_v2.csv 파일의 'transaction_date' 컬럼을 보면 거래일자가 20170228~20170331 이외의 데이터들이 섞여있어서 이상치로 판단 후 제거<br/>
    
결과 : filtered_transactions_v2.csv 데이터 개수 : 1431009  -> 1150924<br/><br/><br/>

- labelmapping.py

msno 값을 label 인코딩 해둔 members_encoded.csv 파일을 불러와 filtered_transactions_v2.csv 파일에 적용하여<br/>
msno 값을 숫자로 변환하고, members_v3.csv (유저정보) 에 없는 msno 값을 가진 데이터를 제거<br/>

결과 : filter_and_labeled_transactions_v2.csv 데이터 개수 : 1150924 -> 1027895<br/><br/><br/>

    
##### transaction.csv 에 대한 전처리 내용 
- labelmapping.py
msno 값을 label 인코딩 해둔 members_encoded.csv 파일을 불러와 filtered_transactions.csv 파일에 적용<br/>
msno 값을 숫자로 변환하고, members_v3.csv (유저정보) 에 없는 msno 값을 가진 데이터를 제거<br/>

결과 : labeled_transactions.csv 데이터 개수 : 21547745 -> 18891703<br/><br/><br/>


- concat.py
    
filter_and_labeled_transactions_v2.csv 와 labeled_transactions.csv 를 concat<br/>
    
결과 : merged_transactions.csv 데이터 개수 : 1027895 + 18891703 -> 19919598<br/><br/><br/>


- merged_transactions_preprocessing.py

merged_transactions.csv 에서 transaction_date 가 membership_expire_date 보다 큰 값(이상치) 제거. 

결과 :  final_merged_transactions.csv 데이터 개수 : 19919598  -> 19779157<br/><br/><br/>


- transaction_processing.py
    
final_merged_transactions.csv 에서 msno_encoded의 타입을 int 형으로 바꾸고 컬럼명을 'msno'로 저장 후, msno_encoded 컬럼 제거.

merged_transactions.csv 파일의 컬럼 중.
1)payment_list_price 보다 actual_amount_paid 가 큰 데이터 들을 제거
2)payment_plan_id 컬럼 제거
 
msno_encoded를 기준으로 그룹화 해서

0)transaction_date 값 중 max 값을 저장. 
1)거래 횟수를 저장해두는 transaction_count 컬럼 생성
2)is_cancel 의 수를 저장해두는 is_cancel_sum 컬럼 생성
3)is_cancel 의 평균을 저장해두는 is_cancel_mean 컬럼 생성
4)actual_amount_paid의 총합을 저장하는 actual_amount_paid_sum 컬럼 생성
5)is_auto_renew 의 평균을 저장한 is_auto_renew_mean 컬럼 생성
6)is_cancel == 0 인 데이터만 필터링하여 plan_days_sum 컬럼 생성 (구독 취소하는 경우의 plan_days를 세지 않기 위함)

추가)  
actual_amount_paid_sum 값이 0 초과인 데이터만 추출(기간 동안 총 결제 금액이 0인 유저 제거 위함)
    
결과 : final_processed_transactions.csv  데이터 개수 : 19919598 -> 1551863<br/><br/><br/>


##### members_v3.csv 에 대한 전처리 내용 
    
- member_preprocessing.py
members_encoded2.csv(members_v3 파일에서 msno값을 labelencoding 한 데이터)의 데이터 개수가 6769473, 이중 gender의 결측치가  4429505 개로 확인되어 gender 컬럼 제거 

결과 : final_members.csv 데이터 개수 : 6769473<br/><br/><br/>


##### members_v3.csv + final_processed_transactions.csv 병합 후 전처리
- merge_transac+member.py
final_members.csv 파일과 final_processed_transactions.csv 파일을 msno를 기준으로 병합 

결과 :  merged_member_transaction_data.csv 데이터 개수 : 1551864<br/><br/><br/>


- preprocessing_member_transaction.py
registration_init_time > transaction_date_max 인 데이터 제거 

결과 :  데이터 개수 : 1551863 -> 1340063<br/><br/><br/>


##### train_encoded.csv + final_merged_member_transaction_data.csv + user_logs_encoded_merged_all.csv 병합
-merge_final.py
train_encoded.csv + final_merged_member_transaction_data.csv + user_logs_encoded_merged_all.csv 세 개의 파일을 'msno' 기준으로 병합

결과 : realrealreal_final_data.csv  데이터 개수 : 839941<br/><br/><br/>

    
-rrrr_final.py
<br/>
![Image](https://github.com/user-attachments/assets/8986b43f-0997-46bb-8ff8-6f33ffddd47b)
<br/>
bd(나이) 10세 이상 80세 이하인 데이터만 추출
    
결과 : rrrr_final_data.csv 데이터 개수 : 839941 -> 275465<br/><br/><br/>

### UnderSampling 적용 
**오버샘플링이 아닌 언더샘플링 적용 이유**
- 이탈 사용자의 데이터 개수가 전처리 후 25612개로 충분하다고 판단
- 오버샘플링을 하며 인위적인 데이터를 만드는 것보다 원본 데이터를 유지하며 학습하는 것이 더 신뢰도가 있을 것이라 판단<br/><br/>
  
rrrr_final_data.csv 의 데이터 비율은 아래와 같다. 
    
is_churn<br/>
0    249853<br/>
1     25612<br/>

약 10:1 로, 데이터 불균형이 상당하여 3:1로 조정하여 언더샘플링을 진행했다.<br/>
- 판단 기준<br/>(https://www.dbpia.co.kr/journal/detail?nodeId=T15485105)<br/>(https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001273099)<br/>

-undersampling.py
  
is_churn<br/>
0    76836<br/>
1    25612<br/>

결과 : undersampling_3_1_data.csv<br/><br/><br/>


-undersam_preprocessing.py<br/><br/>
'actual_amount_paid_sum'을 'transaction_count'로 나눈 새로운 컬럼 추가
'payment_plan_days_sum'을 'transaction_count'로 나눈 새로운 컬럼 추가

결과 : 2_undersampling_3_1_data.csv<br/><br/><br/>


     
---
### 인공지능 학습 결과



---
### Insights

---
### 한 줄 회고

  
