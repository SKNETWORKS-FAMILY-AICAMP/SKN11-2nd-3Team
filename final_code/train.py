import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, StratifiedKFold, RandomizedSearchCV
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score, precision_score, roc_auc_score, roc_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import xgboost as xgb
import lightgbm as lgb
from scipy.stats import randint, uniform

# 데이터 로드
df = pd.read_csv('./data/real_final_data.csv')

# 피처에서 타겟 컬럼 + 불필요 컬럼 제거
X = df.drop(columns = ['is_churn','msno','start_date','end_date','membership_expire_date','is_cancel','num_25','num_50','num_75','num_985','num_100'])
y = df['is_churn']

# 피처 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 스케일링한 것을 다시 DataFrame으로 변환
X_scaled = pd.DataFrame(X_scaled, index=X.index, columns=X.columns)

# Stratified K-Fold 설정
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 모델 리스트
models = {
    "RandomForest": RandomForestClassifier(),
    "XGBoost": xgb.XGBClassifier(use_label_encoder=False, eval_metric="logloss"),
    "LightGBM": lgb.LGBMClassifier(),
    "SVM": SVC(probability=True),  # SVM에서 ROC 계산을 위해 probability=True 설정
    "LogisticRegression": LogisticRegression()
}

# 하이퍼파라미터 공간 설정 (각 모델에 대해)
param_grids = {
    "RandomForest": {
        "n_estimators": randint(100, 1000),
        "max_depth": randint(5, 20),
        "min_samples_split": randint(2, 10),
        "min_samples_leaf": randint(1, 10)
    },
    "XGBoost": {
        "n_estimators": randint(100, 1000),
        "learning_rate": uniform(0.01, 0.3),
        "max_depth": randint(3, 15),
        "subsample": uniform(0.5, 1.0),
        "colsample_bytree": uniform(0.5, 1.0)
    },
    "LightGBM": {
        "n_estimators": randint(100, 1000),
        "learning_rate": uniform(0.01, 0.3),
        "num_leaves": randint(20, 100),
        "max_depth": randint(3, 15),
        "subsample": uniform(0.5, 1.0),
        "colsample_bytree": uniform(0.5, 1.0)
    },
    "SVM": {
        "C": uniform(0.1, 10),
        "kernel": ["linear", "rbf"],
        "gamma": ["scale", "auto"]
    },
    "LogisticRegression": {
        "C": uniform(0.1, 10),
        "penalty": ["l2"],
        "solver": ["liblinear", "saga"]
    }
}

# 결과 저장용 변수
results = {
    "Model": [],
    "Accuracy": [],
    "Precision": [],
    "Recall": [],
    "F1-Score": [],
    "ROC-AUC": []
}

# 모델 학습 및 하이퍼파라미터 튜닝
for model_name, model in models.items():
    print(f"Training and tuning {model_name}...")
    
    # RandomizedSearchCV로 하이퍼파라미터 튜닝
    random_search = RandomizedSearchCV(
        model,
        param_distributions=param_grids[model_name],
        n_iter=3,  # 최대 50번의 랜덤 탐색
        cv=skf,
        scoring="roc_auc",
        random_state=42,
        n_jobs=-1
    )
    
    # 교차검증을 통한 학습
    accuracies = []
    precisions = []
    recalls = []
    f1_scores = []
    roc_aucs = []
    
    for train_idx, val_idx in skf.split(X_scaled, y):
        X_train, X_val = X_scaled.iloc[train_idx], X_scaled.iloc[val_idx]
        y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]
        
        # 하이퍼파라미터 튜닝 후 모델 학습
        random_search.fit(X_train, y_train)
        
        # 예측
        y_pred = random_search.best_estimator_.predict(X_val)
        y_prob = random_search.best_estimator_.predict_proba(X_val)[:, 1]  # ROC AUC를 위한 확률값
        
        # 평가 지표 계산
        accuracies.append(accuracy_score(y_val, y_pred))
        precisions.append(precision_score(y_val, y_pred))
        recalls.append(recall_score(y_val, y_pred))
        f1_scores.append(f1_score(y_val, y_pred))
        roc_aucs.append(roc_auc_score(y_val, y_prob))
    
    # 결과 저장
    results["Model"].append(model_name)
    results["Accuracy"].append(np.mean(accuracies))
    results["Precision"].append(np.mean(precisions))
    results["Recall"].append(np.mean(recalls))
    results["F1-Score"].append(np.mean(f1_scores))
    results["ROC-AUC"].append(np.mean(roc_aucs))

# 결과를 데이터프레임으로 변환
results_df = pd.DataFrame(results)
print(results_df)

# 성능 평가 결과 시각화
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Accuracy, Precision, Recall, F1-Score 막대그래프
axes[0, 0].bar(results_df["Model"], results_df["Accuracy"], color='royalblue')
axes[0, 0].set_title('Accuracy')
axes[0, 1].bar(results_df["Model"], results_df["Precision"], color='salmon')
axes[0, 1].set_title('Precision')
axes[1, 0].bar(results_df["Model"], results_df["Recall"], color='seagreen')
axes[1, 0].set_title('Recall')
axes[1, 1].bar(results_df["Model"], results_df["F1-Score"], color='orange')
axes[1, 1].set_title('F1-Score')

plt.tight_layout()
plt.show()

# ROC-AUC Curve 시각화
plt.figure(figsize=(8, 6))

for model_name, model in models.items():
    fpr, tpr, _ = roc_curve(y, random_search.best_estimator_.predict_proba(X_scaled)[:, 1])
    plt.plot(fpr, tpr, label=f'{model_name} (AUC = {roc_auc_score(y, random_search.best_estimator_.predict_proba(X_scaled)[:, 1]):.2f})')

plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.title('ROC-AUC Curve')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend()
plt.show()
