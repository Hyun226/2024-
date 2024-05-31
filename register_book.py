import pyodbc

def registerbook():
    ## 데이터 베이스 불러오기 the_l 부분 본인 컴퓨터 사용자 명으로 변경
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hyun\Desktop\Database1.accdb;')
    cursor = conn.cursor()

    # Book 테이블의 생성
    cursor.execute('CREATE TABLE Book(ID int primary key, 서명 char(50), 작가 char(30), 출판사 char(30), 출판년도 int, 쪽수 int, 상태 char(10), 대출자 char(30), 예약자 char(30));')

    ## book.txt 파일에서 불러와서 db에 저장
    book_data = open(r"C:\Users\Hyun\Desktop\book.txt", 'r')
    for word in book_data:
        list_word = word.replace("\n", "").split(' ')
        id_n = int(list_word[0])
        서명 = list_word[1]
        작가 = list_word[2]
        출판사 = list_word[3]
        출판년도 = int(list_word[4])
        쪽수 = int(list_word[5])
        
        # book.txt 파일 내에 상태, 대출자, 예약자가 존재하지 않을 수도 있기 때문에
        # 예외 처리문을 통해 존재한다면 넣어주고, 존재하지 않는다면 "없음"을 넣어주도록 하였음
        try:
            상태 = list_word[6]
        except:
            상태 = "없음"
        try:
            대출자 = list_word[7]
        except:
            대출자 = "없음"
        try:
            예약자 = list_word[8]
        except:
            예약자 = "없음"

        # book테이블에 레코드 추가하기
        insert_query = "INSERT INTO Book (ID, 서명, 작가, 출판사, 출판년도, 쪽수, 상태, 대출자, 예약자) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (id_n, 서명, 작가, 출판사, 출판년도, 쪽수, 상태, 대출자, 예약자))

    # 텍스트 파일 닫기
    book_data.close()

    # db파일 저장 및 닫기
    conn.commit()
    cursor.close()
    conn.close()
