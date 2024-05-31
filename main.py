from user import User   # 같은 디렉토리상의 user.py 파일에서 User 클래스를 임포트
from book import Book   # 같은 디렉토리상의 book.py 파일에서 Book 클래스를 임포트

# 현재날짜 (대출/반납 시)를 불러오는 라이브러리
import datetime
# 데이터 베이스 라이브러리
import pyodbc

import borrow
import search
from register_user import registeruser
from register_book import registerbook

# 유저 테이블이 데이터베이스에 존재하지 않는다면 생성해주기 위한 예외 처리문
# 데이터베이스에 존재한다면 오류가 나오기 때문에 except문의 pass로 아무일도 일어나지 않음
try:
    registeruser()
except:
    pass
# 책 테이블이 데이터베이스에 존재하지 않는다면 생성해주기 위한 예외 처리문
# 데이터베이스에 존재한다면 오류가 나오기 때문에 except문의 pass로 아무일도 일어나지 않음
try:
    registerbook()
except:
    pass

while True:
    print("수행할 작업 선택")
    ans = input("""
    1. 이용자/도서 검색
    2. 대출/반납
    3. 대출/반납 기록 조회
    4. 종료
    :
    """)
    
    # 종료를 선택했을 시, 프로그램 종료
    if ans == "4":
        break
    # 1번 이용자/도서 검색 선택시
    if ans == "1":
        print(search.검색())
    # 2번 대출/반납 선택시
    elif ans == "2":
        ans = input("""
        1. 대출
        2. 반납
        :
        """)
        if ans == "1":
            borrow.대출()
        elif ans == "2":
            borrow.반납()
    # 2번 대출/반납 기록 조회 선택시
    elif ans == "3":
        search.대출반납검색()
