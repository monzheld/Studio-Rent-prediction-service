# Section3/Project/data 에서 실행 

# 터미널에서 pandas 설치
# pip install pandas

# 경고 무시
import warnings
warnings.filterwarnings(action='ignore')

# csv 파일 불러오기
import pandas as pd
df = pd.read_csv('/Users/hsh/Section3/Project/data/studio.csv')

# 결측치 확인
#df.isnull().sum()
#['갱신요구권 사용', '종전계약 보증금 (만원)', '종전계약 월세 (만원)'] 칼럼 삭제
df.drop(['갱신요구권 사용', '종전계약 보증금 (만원)', '종전계약 월세 (만원)'], axis=1, inplace=True)
# 결측치 제거
df.dropna(inplace=True)

# ['시군구'] 칼럼에서 구를 추출해 ['구'] 칼럼 생성
df['구'] = df['시군구'].str.split(' ').str[1]
# ['시군구'] 칼럼에서 동을 추출해 ['동'] 칼럼 생성
df['동'] = df['시군구'].str.split(' ').str[2]

# df의 칼럼명 리스트로 보기
#df.columns.tolist()
# 칼럼 순서 변경, ['시군구'] 칼럼 삭제 
df = df[['구', '동', '번지', '본번', '부번', '단지명', '전월세구분','전용면적(㎡)','계약년월','계약일','보증금(만원)','월세(만원)','층','건축년도','도로명','계약기간','계약구분']]

# ['전월세구분'] 칼럼의 값이 '전세'인 row 삭제 
monthly_df = df[df['전월세구분']!='전세']
# ['전월세구분'] 칼럼 제거
monthly_df.drop(['전월세구분'], axis=1, inplace=True)

# ['건축년도'] 칼럼의 데이터타입 float -> int로 변환 
monthly_df['건축년도'] = monthly_df['건축년도'].astype(int)

# (계약기간 년도로 계산하기) 
# ['계약기간']의 값이 '-'인 row 제거
monthly_df = monthly_df[monthly_df['계약기간']!='-'] 
# ['계약기간']의 값을 기간 시작과 끝으로 나누기 
monthly_df['계약기간'].str.split('~')
# 계약기간 시작
monthly_df['계약기간_시작'] = monthly_df['계약기간'].str.split('~').str[0]
# ['계약기간_시작'] 칼럼 데이터타입 object -> int로 변환
monthly_df['계약기간_시작'] = monthly_df['계약기간_시작'].astype(int)
# 계약기간 끝 
monthly_df['계약기간_끝'] = monthly_df['계약기간'].str.split('~').str[1]
# ['계약기간_끝'] 칼럼 데이터타입 object -> int로 변환
monthly_df['계약기간_끝'] = monthly_df['계약기간_끝'].astype(int)
# 계약기간 년도로 계산하기
monthly_df['계약기간 (년도)'] = (monthly_df['계약기간_끝'] - monthly_df['계약기간_시작'])/100
# ['계약기간 (년도)'] 칼럼 데이터타입 float -> int로 변환 후 ['계약기간'] 칼럼으로 대체
monthly_df['계약기간'] = monthly_df['계약기간 (년도)'].astype(int)

# ['보증금(만원)'] 칼럼 ',' 제거
monthly_df['보증금(만원)'] = monthly_df['보증금(만원)'].str.replace(',', '')
# ['보증금(만원)'] 칼럼 데이터타입 object -> int로 변환
monthly_df['보증금(만원)'] = monthly_df['보증금(만원)'].astype(int)

# ['단지명'] 칼럼 "'" 제거
monthly_df['단지명'] = monthly_df['단지명'].str.replace("'", "")

# 칼럼명 변경 
monthly_df.rename(columns={'전용면적(㎡)':'전용면적', '보증금(만원)':'보증금', '월세(만원)':'월세'}, inplace=True)

# ['전용면적'] 칼럼의 값을 평수로 변환 (1평 = 3.31m)
monthly_df['평수'] = monthly_df['전용면적'] / 3.31
# ['평수'] 칼럼 데이터타입 float -> int로 변환
monthly_df['평수'] = monthly_df['평수'].astype(int)

# 칼럼 순서 변경, 칼럼 제거
monthly_df = monthly_df[['구', '동', '번지', '본번', '부번', '단지명', '평수', '보증금', '월세', '계약기간', '층', '건축년도', '도로명', '계약구분', '계약년월', '계약일']]

# 인덱스 reset
monthly_df = monthly_df.reset_index(drop=True)

# 최종 데이터셋
final_df = monthly_df

# csv 파일로 저장 
final_df.to_csv("/Users/hsh/Section3/Project/data/dataset.csv",index=False)