# 🎵 KKBox(대만 음악 스트리밍 서비스) 사용자 이탈 예측 프로젝트
## Member
<table>
  <thead>
    <td align="center">
        <img src="./readme_img//git_img_jangsu.png" height="150" width="150" alt="jangsoo"/><br /><hr/>
        김장수
      </a><br />
    </td>
    <td align="center">
        <img src="./readme_img//git_img_sunill.png" height="150" width="150" alt="Sungil"/><br /><hr/>
        방성일
      </a><br />
    </td>
    <td align="center">
        <img src="https://github.com/user-attachments/assets/a28f14f0-2e04-4bb9-be4f-2fe81924e523" height="150" width="150" alt="jungsoo"/><br /><hr/>
        배정수
      </a><br />
    </td>
    <td align="center">
      <a href="">
        <img src="./readme_img//git_img_hyeondae.png" height="150" width="150" alt="hyundae"/><br /><hr/>
        이현대
      </a><br />
    </td>
      <td align="center">
      <a href="https://github.com/minjung2266">
        <img src="https://github.com/minjung2266.png" height="150" width="150" alt="minjeong"/><br /><hr/>
        이민정
      </a><br />
    </td>
  </thead>
</table>

---
### 📅 개발 기간
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

<hr>

### EDA
#### 1. 데이터 전처리<br/>
![Image](https://github.com/user-attachments/assets/fe0b94b1-b6eb-49e7-aa27-33c52aac836d)
#### transaction_v2.csv 에 대한 전처리 내용
### user_log 데이터 전처리  
1. 28GB였던 유저 로그 데이터를 1.1GB 크기의 26개 파일로 분리  
2. member 테이블을 라벨인코딩하여 key-value 형태의 JSON으로 저장  
3. 분리된 파일의 user_log 데이터를 `msno`를 기준으로 매핑  
4. 각 user_log 내 중복되는 `userId`를 Groupby하여 중복 제거  
   - 이후, `use_date`(노래를 들은 날짜), `start_date`(처음 들은 날), `end_date`(마지막 들은 날) 컬럼 추가  
5. 모든 user_log를 하나로 합친 후 다시 Groupby하여 4번과 동일한 과정 진행  

### transaction 데이터 전처리  
1. 거래 기록 이후의 추가 기록이 확인되어 이상치로 판단 후 제거  
2. 유저 정보 중 아이디가 없는 데이터 제거  
3. 결제일이 멤버십 만료일 이후인 데이터 제거  

### members 데이터 전처리  
1. `gender` 컬럼의 결측치가 70% 이상으로 확인되어 컬럼 제거  

<br/>
![Image](https://github.com/user-attachments/assets/8986b43f-0997-46bb-8ff8-6f33ffddd47b)
<br/>
bd(나이) 10세 이상 80세 이하인 데이터만 추출
    
결과 : rrrr_final_data.csv 데이터 개수 : 839941 -> 275465<br/><br/><br/>

#### 컬럼 추가 및 제거 정리
1. gender의 결측치가 70% 이상, 컬럼 제거
2. end_date 와 start_date -> use_date 컬럼 추가
3. transaction_date 값 중 max 값을 저장 
4. 거래 횟수 : transaction_count 컬럼 추가
5. is_cancel 의 수 : is_cancel_sum 컬럼 추가
6. is_cancel 의 평균 : is_cancel_mean 컬럼 추가
7. actual_amount_paid의 총합 : actual_amount_paid_sum 컬럼 추가( 0인 값 제거)
8. is_auto_renew 의 평균 : is_auto_renew_mean 컬럼 추가
9. is_cancel == 0 인 데이터 필터링 -> plan_days_sum 컬럼 생성




### UnderSampling 적용 
**오버샘플링이 아닌 언더샘플링 적용 이유**
- 이탈 사용자의 데이터 개수가 전처리 후 25612개로 충분하다고 판단
- 오버샘플링을 하며 인위적인 데이터를 만드는 것보다 원본 데이터를 유지하며 학습하는 것이 더 신뢰도가 있을 것이라 판단<br/><br/>
  
rrrr_final_data.csv 의 데이터 비율은 아래와 같다. 
    
| is_churn | Count  |
|----------|--------|
| 0        | 249853 |
| 1        | 25612  |


약 10:1 로, 데이터 불균형이 상당하여 3:1로 조정하여 언더샘플링을 진행했다.<br/>
- 판단 기준<br/>(https://www.dbpia.co.kr/journal/detail?nodeId=T15485105)<br/>(https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001273099)<br/>

-undersampling.py
  
| is_churn | Count  |
|----------|--------|
| 0        | 76836  |
| 1        | 25612  |


결과 : undersampling_3_1_data.csv<br/><br/><br/>


-undersam_preprocessing.py<br/><br/>
'actual_amount_paid_sum'을 'transaction_count'로 나눈 새로운 컬럼 추가
'payment_plan_days_sum'을 'transaction_count'로 나눈 새로운 컬럼 추가

결과 : 2_undersampling_3_1_data.csv<br/><br/><br/>

##### [ DataSet : 최종 데이터]
| 컬럼명                   | 설명                                                                |
|------------------------|---------------------------------------------------------------------------|
| `msno`                 | 사용자 고유 ID                                                              |
| `is_churn`             | 이탈 여부 (1: 이탈, 0: 유지)                                                 |
| `city`                 | 사용자의 도시 (지역 정보)                                                    |
| `bd`                   | 사용자의 나이 (birth date에서 유추)                                          |
| `registered_via`       | 등록 경로 (앱, 웹, 페이스북 등)                                              |
| `registration_init_time` | 가입한 날짜 (YYYYMMDD 형식)                                                |
| `transaction_count`    | 총 거래 횟수                                                                 |
| `is_cancel_mean`       | 평균적으로 거래가 취소된 비율                                                 |
| `is_auto_renew_mean`   | 자동 갱신 여부 평균 (1: 자동 갱신됨, 0: 아님)                                 |
| `payment_plan_days_sum` | 전체 결제 플랜 일수 합                                                       |
| `num_25`               | 25% 정도 감상한 곡 수                                                         |
| `num_50`               | 50% 정도 감상한 곡 수                                                         |
| `num_75`               | 75% 정도 감상한 곡 수                                                         |
| `num_985`              | 거의 끝까지 (98.5%) 감상한 곡 수                                              |
| `num_100`              | 100% 감상한 곡 수                                                             |
| `total_secs`           | 전체 감상 시간(초 단위)                                                       |
| `use_date`             | 해당 사용자의 데이터가 몇 개의 날짜에 걸쳐 있는지 (사용일 수)                 |

### 데이터 시각화 

![Image](https://github.com/user-attachments/assets/d37b851d-ea2d-4f75-b4f8-0e03c74b6549)


![Image](https://github.com/user-attachments/assets/8ed75916-2dec-4215-99db-9093384f7128)


![Image](https://github.com/user-attachments/assets/386f3e84-7fd4-4ff2-b51c-2e265e0ab0a0)


![Image](https://github.com/user-attachments/assets/d21f3aeb-8f0e-42e6-871d-b6f3da89a443)


![Image](https://github.com/user-attachments/assets/20bba289-9311-4002-834a-2dca5e4d5124)

     
---
### 인공지능 학습 결과

#### Model Performance (Before & After Tuning)

| Model               | Accuracy (Before → After) | Precision (Before → After) | Recall (Before → After) | F1 Score (Before → After) | ROC AUC (Before → After) |
|--------------------|---------------------|----------------------|----------------|-----------------|----------------|
| **LogisticRegression** | 0.8319 → 0.8320  | 0.6814 → 0.6815  | 0.6140 → 0.6142 | 0.6459 → 0.6461  | 0.8739 → 0.8743 |
| **RandomForest**      | 0.8601 → 0.9618  | 0.7606 → 0.9811  | 0.6416 → 0.8638 | 0.6960 → 0.9187  | 0.9190 → 0.9896 |
| **XGBoost**           | 0.8623 → 0.8907  | 0.7565 → 0.8243  | 0.6613 → 0.7145 | 0.7057 → 0.7655  | 0.9225 → 0.9460 |
| **LightGBM**          | 0.8636 → 0.8808  | 0.7794 → 0.8180  | 0.6329 → 0.6721 | 0.6985 → 0.7379  | 0.9237 → 0.9388 |


#### 튜닝 후 모델별 성능 비교
![Image](https://github.com/user-attachments/assets/fca649a4-26c2-49ed-9b8f-11068556577e)
#### 튜닝 후 ROC - CURVE
![Image](https://github.com/user-attachments/assets/798780aa-350f-4db3-9e91-d3b3eae4b690)
#### 모델 별 예측 데이터 수 
![Image](https://github.com/user-attachments/assets/181a7dc1-1ef8-453d-942f-55833b46a0f1) 

- 평가지표, ROC - CURVE 의 결과를 토대로 최종 모델을 **RandomForest**로 선정

#### 특성 중요도 
![Image](https://github.com/user-attachments/assets/c8f43974-9b86-41ba-b922-53192a6fec95)


---
### Insights 및 결론

---
### 한 줄 회고

| 팀원  | 한 줄 회고                 |
|-------|----------------------------|
| 정수  |  |
| 현대  |  |
| 성일  |  |
| 장수  |  |
| 민정  |  |
  
