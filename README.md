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
##  🎯 프로젝트 개요
### 📅 개발 기간
**2025.03.31 ~ 2025.04.01 (총 2일)**

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
   


### WBS

| 내용                     | 기간                  | 담당            |
|--------------------------|----------------------|---------------|
| 프로젝트 주제 설정        | 25.03.31 - 25.03.31  | ALL           |
| 데이터 수집              | 25.03.31 - 25.03.31  | ALL           |
| 데이터 EDA     | 25.03.31 - 25.03.31  | ALL           |
| 데이터 전처리    | 25.03.31 - 25.03.31  | ALL           |
| 모델 선정    | 25.03.31 - 25.03.31  | ALL           |
| 모델 학습 및 평가        | 25.03.31 - 25.04.01  | ALL |
|  README 작성    | 25.03.31 - 25.04.01  | ALL           |
|  발표 준비    | 25.04.01 - 25.04.01  | ALL           |

<hr>

## 📂데이터 구성
### - 데이터소스: [WSDM - KKBox의 Churn Prediction Challenge](https://www.kaggle.com/c/kkbox-churn-prediction-challenge/overview)

#### [ DataSet ]

1. members_v3.csv [유저 테이블]
    - **설명**: 유저의 프로필 정보
    - **컬럼**
        - `msno`: 유저 ID
        - `city`: 도시
        - `bd`: 나이 
        - `gender`: 성별
        - `registered_via`: 가입 경로
        - `registration_init_time`: 가입 날짜 (`%Y%m%d`)
2. train_v2.csv [이탈 여부]
    - **설명**: 유저 ID와 이탈 여부(`is_churn`)가 포함된 학습용 데이터셋 (2017년 2월까지의 데이터 기반)
    - **컬럼**
        - `msno`: 유저 ID
        - `is_churn`: 이탈 여부 ('1' = 이탈 o, '0' = 이탈 x)
3.  transactions.csv / transactions_v2.csv 
    - **설명**: 유저의 **결제 이력**이 담긴 데이터셋
    - **컬럼**
        - `msno`: 유저 ID
        - `payment_method_id`: 결제 방식 ID x
        - `payment_plan_days`: 플랜 기간 (일 기준)
        - `plan_list_price`: 플랜 정가 (NTD)
        - `actual_amount_paid`: 실제 결제 금액 (NTD)
        - `is_auto_renew`: 자동 갱신 여부
        - `transaction_date`: 결제 날짜 (`%Y%m%d`)
        - `membership_expire_date`: 회원 만료일 (`%Y%m%d`)
        - `is_cancel`: 구독 취소 여부
        - discount_amout : 할인율 [1 - (actual_amount_pain / plan_list_price).  mean/sum]


4.  user_logs.csv / user_logs_v2.csv
    - **설명**: 유저의 **일일 음악 재생 로그**를 담은 데이터셋 (2017년 2월까지).
    - **컬럼**
      - `msno`: 유저 ID
      - `date`:  `%Y%m%d` 형식의 날짜
      - `num_25`: 25% 미만 청취 된 노래의 개수
      - `num_50`: 25 ~ 50% 청취 된 노래의 개수
      - `num_75`: 50 ~ 75% 청취 된 노래의 개수
      - `num_985`: 75 ~ 98.5% 청취 된 노래의 개수
      - `num_100`: 98.5~100% 청취 된 노래의 개수
      - `num_unq`: 청취한 노래의 개수
      - `total_secs`: 총 재생 시간(초)

### 기술 스택
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
#### 이상치 확인

<img src="./readme_vi//box_plot_for_all.png">

# 전처리

## members_v3.csv [유저]  
 1. 모든 테이블에 msno (userId값)이 암호화된 텍스트로 되어 있기 때문에 데이터의 크기가 커짐.
 2. 데이터의 크기를 줄이기 위해 msno 컬럼의 값을 Label 인코딩을 통해 1부터 시작하는 Int 자료형으로 변경.
 3. 변경된 데이터를 이전 값을 key 이후 값을 value로 가지는 json 형태로 저장
 
## user_log.csv 에 대한 데이터 전처리
  1. 28GB의 데이터를 한번에 처리 불가능. => 메모리 문제
  2. 1500만 row씩[1.1GB] 26개 파일로 분리
  3. 분리된 파일의 user_log 데이터를 `msno`를 기준으로 Json 파일을 활용해 매핑  
  4. 각 user_log 내 중복되는 `userId(msno)`를 Groupby하여 중복 제거  
  5. `use_date`(노래를 시청 날짜), `start_date`(처음 시청한 날), `end_date`(마지막 시청한 날) 컬럼 추가  
  6. 모든 user_log를 하나로 합친 후 다시 Groupby하여 5번과 동일한 과정 진행  

## transaction [결제 이력] 

  1. label.json을 바탕으로 transaction 파일의 msno 값을 인코딩
  2. transaction에는 member에는 없는 유저를 결측치로 판단하여 제거
  3. 데이터 컬럼 명세를 바탕으로 각 사용자별 결제 데이터를 하나의 row로 시계열 데이터로 저장됨을 확인.
  4. v1과 v2의 차이는 2017년 2월 28일을 기준으로 전후 데이터 이면 v2는 2017년 3월 31일 까지의 거래 기록.
  5. v2에서 transaction_date 컬럼의 거래 일자에 2017년 2월 28일 이전 데이터를 확인 하여 해당 데이터를 이상치로 판단 하여 제거함.
  6. pandas의 concat를 활용하여 v1 v2 결합
  7. transaction_date(결제 날짜)가 membership_expire_date(멤버십 만료 날짜) 보다 큰 값은 결제를 했지만 맴버십 날짜가 갱신되지 않은 데이터라고 판단하여 이상치 데이터로 제거.
  8. payment_list_price(정가) 보다 actual_amount_paid(실 구매가) 가 큰 데이터 들은 이상치라고 판단하여 제거 
  9. payment_plan_id (결제 방식)에 대한 값은 숫자로 되어 있고 해당 값이 어떤걸 의미하는지에 대한 인사이트를 뽑을 수 없기 때문에 해당 컬럼 제거
  10. actual_amount_paid의 값이 0인 데이터를 제거
  11. 거래 횟수를 저장해두는 transaction_count 컬럼 생성.
  12. is_cancel == 0 인 데이터만 필터링하여 plan_days_sum 컬럼 생성 (구독 취소하는 경우의 plan_days를 세지 않기 위함)
  13. transaction_date 값 중 max 값을 저장.
  14. is_cancel 의 수를 저장해두는 is_cancel_sum 컬럼 생성
  15. is_cancel 의 평균을 저장해두는 is_cancel_mean 컬럼 생성
  16. actual_amount_paid의 총합을 저장하는 actual_amount_paid_sum 컬럼 생성
  17. is_auto_renew 의 평균을 저장한 is_auto_renew_mean 컬럼 생성
  18. _sum 값이 0인 유저는 결제 했지만 0원
  19. actual_amount_paid_sum(실 결제 가격)을 transaction_count(결제 횟수)로 나눈 새로운 컬럼 추가
  20. payment_plan_days_sum을 transaction_count로 나눈 새로운 컬럼 추가
     
## 유저 데이터와 결제 데이터 병합(transaction + members)
1. final_members.csv 파일과 final_processed_transactions.csv 파일을 msno를 기준으로 병합 
2. registration_init_time(플랫폼 가입 날짜)가 transaction_date_max(마지막 결제일)보다 일찍 결제한 데이터는 해당 사용자가 가입 이전에 결제를 할 수 없기 때문에 해당 데이터를 이상치로 판단하여 삭제
 
## 전체 파일 병합
1. train_encoded.csv + final_merged_member_transaction_data.csv + user_logs_encoded_merged_all.csv 세 개의 파일을 'msno' 기준으로 병합
2. 고객의 나이를 10 ~ 80세 사이로 전처리


# 최종 데이터 파일    
## [최종 데이터 파일 31.5MB](./data/rrrr_final_data.csv)

# UnderSampling 적용 

| **UnderSampling 적용 전** |          |
|---------------------------|----------|
| is_churn (이탈)           | count    |
|---------------------------|----------|
| 0                         | 249853   |
| 1                         | 25612    |

```위 데이터를 바탕으로 이탈(1)과 이탈이 아닌(0) 데이터의 데이터 불균형이 10배 차이가 발생하는데 이를 해결하기 위한 방법으로 Under 샘플링을 적용.```

 **오버샘플링이 아닌 언더샘플링 적용 이유**
 1. 이탈 사용자의 데이터 개수가 전처리 후 25612개로 충분하다고 판단
 2. 오버샘플링을 하며 인위적인 데이터를 만드는 것보다 원본 데이터를 유지하며 학습하는 것이 더 신뢰도가 있을 것이라 판단하였고 약 10:1 를 보이는 데이터 불균형을 언더 샘플링을 통해 3:1로 조정.

 **UnderSampling 적용 후**
 | **UnderSampling 적용 전** |          |
|---------------------------|----------|
| is_churn (이탈)           | count    |
|---------------------------|----------|
| 0               | 76836  |
| 1               | 25612   |



## 참고 자료
1. [최적 샘플링 비율 탐색을 통한 불균형 자료 문제 해결 방안](https://www.dbpia.co.kr/journal/detail?nodeId=T15485105)
2. [불균형 데이터에 대한 오버샘플링 효과 연구](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001273099)
 


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

<img src="./readme_vi//churn_non_churn.png">

<img src="./readme_vi//auto_renew_vs_churn.png">

<img src="./readme_vi//use_date_distribution.png">

<img src="./readme_vi//transaction_count.png">

<img src="./readme_vi//listen_percentage_vs_churn.png">

     
---
### 인공지능 학습 결과

#### 하이퍼 파라미터 (RandomSearchCV)
- 대용량 데이터를 학습하는데 시간이 많이 소요되어 RandomSearchCV 사용
![Image](https://github.com/user-attachments/assets/c38f7bed-00b1-4e97-9669-459c3e3aa0d9) 

## RandomizedSearchCV를 사용하여 최적의 하이퍼 파라미터 확인 후 적용

| Model               | Accuracy (Before → After) | Precision (Before → After) | Recall (Before → After) | F1 Score (Before → After) | ROC AUC (Before → After) |
|--------------------|---------------------|----------------------|----------------|-----------------|----------------|
| **LogisticRegression** | 0.8319 → 0.8320  | 0.6814 → 0.6815  | 0.6140 → 0.6142 | 0.6459 → 0.6461  | 0.8739 → 0.8743 |
| **RandomForest**      | 0.8601 → 0.9618  | 0.7606 → 0.9811  | 0.6416 → 0.8638 | 0.6960 → 0.9187  | 0.9190 → 0.9896 |
| **XGBoost**           | 0.8623 → 0.8907  | 0.7565 → 0.8243  | 0.6613 → 0.7145 | 0.7057 → 0.7655  | 0.9225 → 0.9460 |
| **LightGBM**          | 0.8636 → 0.8808  | 0.7794 → 0.8180  | 0.6329 → 0.6721 | 0.6985 → 0.7379  | 0.9237 → 0.9388 |

### 최적의 하이퍼 파라미터
![](https://github-production-user-asset-6210df.s3.amazonaws.com/112079783/428911564-841f452a-87ea-4e26-9352-06369ea47d06.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250401%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250401T080154Z&X-Amz-Expires=300&X-Amz-Signature=5a85d67250512c37af7f0f71eecd7c4c7d8da581f181e83099f4255ed12f987b&X-Amz-SignedHeaders=host)

#### 튜닝 후 모델별 성능 비교
![Image](https://github.com/user-attachments/assets/fca649a4-26c2-49ed-9b8f-11068556577e)
#### 튜닝 후 ROC - CURVE
![Image](https://github.com/user-attachments/assets/798780aa-350f-4db3-9e91-d3b3eae4b690)
#### 모델 별 예측 데이터 수 
![Image](https://github.com/user-attachments/assets/181a7dc1-1ef8-453d-942f-55833b46a0f1) 

- 평가지표, ROC - CURVE 의 결과를 토대로 최종 모델을 **RandomForest**로 선정

#### 특성 중요도 
<img src="./readme_vi//feature_importances.png">


---
### Insights 및 결론
- 결제 취소율을 줄이기 위해서는 취소 정책을 더욱 강하게 하면 자동 결제율은 줄어들겠지만 이탈을 줄일 수 있다.
- 자동결제율이 높을수록 고객 이탈이 적은 경향을 보이는데, 이를 바탕으로 자동 결제율이 감소하는 문제를 해결하기 위해 자동결제를 유지하면 요금제 할인 등 프로모션을 진행하면 고객 이탈을 방지할 수 있다. 
---
### 한 줄 회고

| 팀원  |               한 줄 회고                 |
|-------|----------------------------|
| 정수  | 대용량 데이터를 처음 다뤄봐서 정제에만 시간이 오래 걸렸습니다. 여러 데이터 파일을 병합하고 정제하는 과정이 재미있었고, 분류 모델을 사용하며 과적합을 해결해보고자 여러 방법을 시도해봤지만 해결하지 못한 점과 인사이트 도출이 아쉬웠습니다 |
| 현대  | 대용량 실 데이터를 다룬 경험이 의미 있었다고 생각합니다.다만 데이터의 크기가 컸지만 로그 자체에 이상 데이터도 많았고 전처리에 더 많은 시간을 쓰지 못한점이 아쉬웠다  |
| 성일  | 여러 분류 모델과 데이터 전처리를 진행하며 수업하며 배운 내용들을 다질 수 있어 좋았다.  |
| 장수  | user_logs.csv 같은 경우에는 파일 크기가 약 30GB로, 데이터 개수만 3억 개가 넘기 때문에 VSCode 에서 파일을 불러오는 것 조차 거의 불가능했습니다. 따라서 이 파일을 분할하여 전처리를 진행했는데 새로운 경험이었고, 그 외의 파일에 대해서도 대용량 데이터를 처리하면서 고려해야 할 점이 많아서 흥미로웠습니다. 그리고 학습 할 때 시간이 많이 소요되었는데 학습 시간을 단축시키는 방법에 대해서도 앞으로 고민해보고 싶습니다.  |
| 민정  | 약 30GB에 달하는 user_log 데이터를 효율적으로 다루기 위해 다양한 전처리 전략을 시도했했지만, 하이퍼파라미터 튜닝에도 모델의 과적합이 해결되지 않아 아쉬웠습니다. 

  
