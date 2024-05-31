def 대출():
    import search
    import datetime
    import pyodbc

    print("대출하는 이용자를 검색해주세요")
    buser = search.검색()
    if buser == 0:
        ans = input("회원등록 하시겠습니까? y/n: ")
        if ans == 'y':
            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hyun\Desktop\Database1.accdb;')
            cursor = conn.cursor()

            # id값 가져오기
            select_query = "SELECT ID FROM Book"
            cursor.execute(select_query)
            rows = cursor.fetchall()
            book_ids = [row[0] for row in rows]

            id_n = book_ids[-1] + 1
            이름 = input("이름: ")
            성별 = input("성별: ")
            주소 = input("주소: ")
            직업 = input("직업: ")
            출생년도 = int(input("출생년도: "))

            insert_query = "INSERT INTO User (ID, 이름, 성별, 주소, 직업, 출생년도) VALUES (?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_query, (id_n, 이름, 성별, 주소, 직업, 출생년도))
            # db파일 저장 및 닫기
            conn.commit()
            cursor.close()
            conn.close()
            print("회원등록 되었습니다")
        return 0

    print("대출할 책을 검색해주세요")
    bbook = search.검색()
    if bbook == 0:
        ans = input("책을 구입 하시겠습니까?: y/n: ")
        if ans == "y":
            서명 = input("서명: ")
            작가 = input("작가: ")
            출판사 = input("출판사: ")
            출판년도 = input("출판년도: ")
            쪽수 = input("쪽수: ")
            print("구매 예정 목록에 책을 추가했습니다")
            use = open("구매 예정 목록.txt", 'w')
            use.write(서명 + " ")
            use.write(작가 + " ")
            use.write(출판사 + " ")
            use.write(출판년도 + " ")
            use.write(쪽수 + "\n")
            use.close()
        return 0

    print("대출자")
    print(buser)

    print("대출도서")
    print(bbook)

    print("대출일자")
    now = datetime.datetime.now()
    print(str(now)[:10])

    print("반납일")
    date = now + datetime.timedelta(weeks=2)
    date = str(date)
    print(date[:10])

    print("대출이 완료되었습니다")

    use = open("use.txt", 'a')
    use.write(str(buser[0]) + "|")
    use.write(str(bbook[0]) + "|")
    use.write(str(now)[:10] + "|")
    use.write(date[:10] + "\n")
    use.close()


def 반납():
    import search
    import datetime
    import pyodbc

    print("반납하는 이용자를 검색해주세요")
    buser = search.검색()

    print("반납할 책을 검색해주세요")
    bbook = search.검색()

    print("반납자")
    print(buser)

    print("반납도서")
    print(bbook)

    print("대출일자")
    now = datetime.datetime.now()
    date = now - datetime.timedelta(weeks=2)
    date = str(date)
    print(date[:10])

    print("반납일")
    print(str(now)[:10])

    print("반납이 완료되었습니다")

    use = open("use.txt", 'a')
    use.write(str(buser[0]) + "|")
    use.write(str(bbook[0]) + "|")
    use.write(date[:10] + "|")
    use.write(str(now)[:10] + "\n")
    use.close()
