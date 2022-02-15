# /Section3/Project/data 에서 실행

# 터미널에서 sklearn 설치 
# pip install sklearn 

# csv 파일 불러오기 
import pandas as pd
data = pd.read_csv('/Users/hsh/Section3/Project/data/dataset.csv')

# 타겟 변수 설정 
target = '월세'

# Mean target 인코딩으로 ['구'] 칼럼 인코딩 
Mean_target_encoded = data.groupby('구')[target].mean()
data['구_encoded'] = data['구'].map(Mean_target_encoded)

# 특성, 타겟 변수 설정
features = ['구_encoded', '평수', '계약기간', '건축년도']
#target = '월세'
# 훈련/테스트셋으로 분할
from sklearn.model_selection import train_test_split 
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size = 0.2, train_size = 0.8, random_state = 2)

# 다중선형회귀모델 모델링 
from sklearn.linear_model import LinearRegression
# 예측모델 인스턴스
model = LinearRegression()
# 모델 학습
model.fit(X_train, y_train)

# 테스트셋에 적용
y_pred = model.predict(X_test)

# 평가지표: r2_score
# 실제 관측값의 분산대비 예측값의 분산을 계산하여 데이터 예측의 정확도 성능을 측정
from sklearn.metrics import r2_score
print('r2_score:', r2_score(y_test, y_pred))

# 피클링
import pickle

with open('model.pkl','wb') as pickle_file:
    pickle.dump(model, pickle_file)