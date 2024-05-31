import pyodbc

def registeruser():
    ## 데이터 베이스 불러오기 the_l 부분 본인 컴퓨터 사용자 명으로 변경
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hyun\Desktop\Database1.accdb;')
    cursor = conn.cursor()

    # User 테이블의 생성
    cursor.execute('CREATE TABLE User(ID int primary key, 이름 char(50), 성별 char(10), 주소 char(30), 직업 char(10), 출생년도 int);')

    ## user.txt 파일에서 불러와서 db에 저장
    user_data = open(r"C:\Users\Hyun\Desktop\user.txt", 'r')
    for word in user_data:
        list_word = word.replace("\n", "").split(' ')
        id_n = int(list_word[0])
        이름 = list_word[1]
        성별 = list_word[2]
        주소 = list_word[3]
        직업 = list_word[4]
        출생년도 = int(list_word[5])

        # user테이블에 레코드 추가하기
        insert_query = "INSERT INTO User (ID, 이름, 성별, 주소, 직업, 출생년도) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (id_n, 이름, 성별, 주소, 직업, 출생년도))

    # 텍스트 파일 닫기
    user_data.close()

    # db파일 저장 및 닫기
    conn.commit()
    cursor.close()
    conn.close()
