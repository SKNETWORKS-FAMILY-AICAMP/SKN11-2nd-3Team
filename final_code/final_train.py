import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score, precision_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, StratifiedKFold

from sklearn.svm import SVC
import xgboost as xgb
import lightgbm as lgb

# 파일 불러오기
df = pd.read_csv('rrrr_final_data.csv')
# class_counts = df['is_churn'].value_counts()
# print(class_counts)

# 피처에서 타겟 컬럼 + 불필요 컬럼 제거
X = df.drop(columns = ['is_churn','msno','start_date','end_date'])
# X = df.drop(columns=['msno','is_churn','registration_init_time','start_date','end_date'])
y = df['is_churn']

# 피처 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(X_scaled,y,test_size=0.2,random_state=42)



#Lightbgm
model = lgb.LGBMClassifier(random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("LightGBM 정확도:", accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))
#로지스틱 회귀
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Logistic Regression 정확도:", accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))

#랜덤 포레스트
model = RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Random Forest 정확도:", accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))

#SVC
model = SVC(kernel='rbf')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("SVM 정확도:", accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))

#XGBoost
model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("XGBoost 정확도:", accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))