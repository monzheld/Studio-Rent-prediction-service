# 터미널에서 psycopg2 설치
# pip install psycopg2-binary

import psycopg2
import csv 

# Postgre 데이터베이스 서버와 연결
# Postgre 서버: elephantDB 
conn = psycopg2.connect(
    host="arjuna.db.elephantsql.com",
    database="qfavrvth",
    user="qfavrvth",
    password="gk5ywvTdY36oxJFvBJCnItRIMxsGPiQ5")

# 커서 생성
cur = conn.cursor()

# table 생성
cur.execute('DROP TABLE IF EXISTS studio;')

cur.execute("""CREATE TABLE studio (
                Id INTEGER PRIMARY KEY NOT NULL,
				구 VARCHAR(32),
				동 VARCHAR(32),
                번지 VARCHAR(32),
                본번 INTEGER,
                부번 INTEGER,
                단지명 VARCHAR(32),
                평수 INTEGER,
                보증금 INTEGER,
                월세 INTEGER,
                계약기간 INTEGER,
                층 INTEGER,
                건축년도 INTEGER,
                도로명 VARCHAR(32),
                계약구분 VARCHAR(32),
                계약년월 INTEGER,
                계약일 INTEGER
                );
			""")

# 데이터베이스에 저장할 csv file
with open('dataset.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = [x for x in reader] # csv 파일을 리스트로 저장

# header 삭제
data.pop(0)

# Id 추가
for i in range(len(data)):
    data[i].insert(0, i)

# 다중 삽입문을 위한 빈 텍스트 생성
insert_text = ''

# 튜플형태로 변경하고 ','로 나누어 데이터 삽입
for i,text in enumerate(data):
    insert_text += str(tuple(text)) # 튜플로 변경하여 저장
    insert_text += ',' # ','로 데이터 나눔

insert_text = insert_text[:-1] # 삽입문의 마지막 ',' 제거


# 삽입문 전송
cur.execute("INSERT INTO studio (Id, 구, 동, 번지, 본번, 부번, 단지명, 평수, 보증금, 월세, 계약기간, 층, 건축년도, 도로명, 계약구분, 계약년월, 계약일) VALUES {};".format(insert_text))

# 데이터 베이스에 내용 전송
conn.commit()

# 데이터 베이스에 제대로 저장되었는지 확인
cur.execute("SELECT * FROM studio")
result = cur.fetchall()
print(result[-3:]) # 마지막 3개 row 출력 

# 데이터 베이스 연결 종료
conn.close()
