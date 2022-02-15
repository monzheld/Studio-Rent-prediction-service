# Flask 설치 
# pip install flask

from flask import Flask, render_template, request 
import pickle
import numpy as np

model = None
with open('model.pkl','rb') as pickle_file:
   model = pickle.load(pickle_file)


app = Flask(__name__)

# index 페이지 
@app.route('/')
def index():
    return render_template('index.html')


# predict
@app.route('/predict', methods=['GET'])
def make_prediction():
    # input 값 받아오기 
    district = request.args.get("district") 
    space = int(request.args.get("space"))
    term = int(request.args.get("term"))
    condstruction = int(request.args.get("condstruction"))

    # '구' encoding 값으로 변환
    if district == '강남구':
      ans = 80.63615023
    elif district == '강동구':
      ans = 58.40028902
    elif district == '강북구':
      ans = 55.21052632
    elif district == '강서구':
      ans = 50.74583532
    elif district == '관악구':
      ans = 46.50680272
    elif district == '광진구':
      ans = 62.3667426
    elif district == '구로구':
      ans = 54.23896499
    elif district == '금천구':
      ans = 50.06082725
    elif district == '노원구':
      ans = 52.66666667
    elif district == '도봉구':
      ans = 54.70506912
    elif district == '동대문구':
      ans = 54.9232
    elif district == '동작구':
      ans = 53.77304965
    elif district == '마포구':
      ans = 63.22202949
    elif district == '서대문구':
      ans = 62.74852071
    elif district == '서초구':
      ans = 75.10576923
    elif district == '성동구':
      ans = 62.50788644
    elif district == '성북구':
      ans = 49.99090909
    elif district == '송파구':
      ans = 72.55113636
    elif district == '양천구':
      ans = 82.40265487
    elif district == '영등포구':
      ans = 63.93347193
    elif district == '용산구':
      ans = 79.72093023
    elif district == '은평구':
      ans = 48.66351607
    elif district == '종로구':
      ans = 60.62439024
    elif district == '중구':
      ans = 66.86984127
    else:
      ans = 46.448

    # 모델에 input 값 넣어서 예측 
    arr = np.array([[ans, space, term, condstruction]])
    pred = model.predict(arr)
    return render_template('result.html', data= int(pred))



if __name__ == "__main__":
    app.run(debug=True)
