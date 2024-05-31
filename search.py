def 검색():
    import pyodbc

    while True:
        num = input("""
        검색할 데이터?
        1. 이용자
        2. 도서
        : """)

        ### 이용자 검색
        if num == "1":
            num = input("""
                    검색할 항목은?
                    1. 이름
                    2. 성별
                    3. 출생년도
                    : """)

            # 데이터베이스 연결 설정
            conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hyun\Desktop\Database1.accdb;')
            cursor = conn.cursor()

            # 검색할 값
            search_value = input("검색어를 입력해주세요: ")
						
						## 검색할 항목에서 1. 이름을 선택했을 경우
            if num == "1":
                try:
                    # SELECT 구문
                    # 유저테이블에서 검색할 값으로 입력받은 이름의 유저 정보를 가져옴
                    select_query = "SELECT * FROM User WHERE 이름 = ?"
                    cursor.execute(select_query, (search_value,))
                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력
                    cleaned_rows = []
                    # 가져온 값이의 형태가 "한라현     " 이런식으로 공백이 포함 돼
                    # 공백을 제거해 주기 위한 코드
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    # 가져온 값이 없다면 오류가 나오기 때문에 except문으로 넘어가게됨
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0


            ## 검색할 항목에서 2. 성별을 선택했을 경우
            elif num == "2":
                try:
                    # SELECT 구문
                    # 유저테이블에서 검색할 값으로 입력받은 성별의 유저 정보를 가져옴
                    select_query = "SELECT * FROM User WHERE 성별 = ?"
                    cursor.execute(select_query, (search_value,))

                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력# 가져온 값이의 형태가 "한라현     " 이런식으로 공백이 포함 돼
                    # 공백을 제거해 주기 위한 코드
                   
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0


            elif num == "3":
                try:
                    # SELECT 구문
                    select_query = "SELECT * FROM User WHERE 출생년도 = ?"
                    cursor.execute(select_query, (search_value,))

                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0


            else:
                print("다시 입력해주세요")


        ### 도서 검색
        elif num == "2":
            num = input("""
                    검색할 항목은?
                    1. 서명
                    2. 작가
                    3. 출판사
                    4. 출판년도
                    : """)

            # 데이터베이스 연결 설정
            conn = pyodbc.connect(
                r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hyun\Desktop\Database1.accdb;')
            cursor = conn.cursor()

            # 검색할 값
            search_value = input("검색어를 입력해주세요: ")

            if num == "1":
                try:
                    # SELECT 구문
                    select_query = "SELECT * FROM Book WHERE 서명 = ?"
                    cursor.execute(select_query, (search_value,))

                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0

            elif num == "2":
                try:
                    # SELECT 구문
                    select_query = "SELECT * FROM Book WHERE 작가 = ?"
                    cursor.execute(select_query, (search_value,))

                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0

            elif num == "3":
                try:
                    # SELECT 구문
                    select_query = "SELECT * FROM Book WHERE 출판사 = ?"
                    cursor.execute(select_query, (search_value,))

                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0

            elif num == "4":
                try:
                    # SELECT 구문
                    select_query = "SELECT * FROM Book WHERE 출판년도 = ?"
                    cursor.execute(select_query, (search_value,))

                    # 결과 가져오기
                    rows = cursor.fetchall()

                    # 결과 처리 및 출력
                    cleaned_rows = []
                    for row in rows:
                        cleaned_row = tuple(col.strip() if isinstance(col, str) else col for col in row)
                        cleaned_rows.append(cleaned_row)

                    # 연결 닫기
                    cursor.close()
                    conn.close()
                    # 검색 값 검증
                    cleaned_rows[0]
                    # 검색 값 반환
                    return cleaned_rows

                except:
                    print("검색값이 존재하지 않습니다")
                    return 0

            else:
                print("다시 입력해주세요")

        else:
            print("다시 입력해주세요")


def 대출반납검색():
    ans = input("""
    대출 반납 내역을 조회합니다.
    1. 도서명 조회
    2. 회원명 조회
    """)
    use_list = []
    use_data = open("use.txt", 'r')
    for word in use_data:
        list_word = word.replace("\n", "").split('|')
        use_list.append(list_word)
    use_data.close()

    if ans == "1":
        ans = input("조회할 도서명: ")
        for word in use_list:
            if ans in word[1]:
                print("대출자: " + word[0])
                print("대출도서: " + word[1])
                print("대출일자: " + word[2])
                print("반납일자: " + word[3])

    elif ans == "2":
        ans = input("조회할 회원명: ")
        for word in use_list:
            if ans in word[0]:
                print("대출자: " + word[0])
                print("대출도서: " + word[1])
                print("대출일자: " + word[2])
                print("반납일자: " + word[3])
