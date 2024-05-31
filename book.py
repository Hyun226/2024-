class Book:
    # 책 등록
    # __init__는 클래스를 생성할 때, 실행되는 함수
    def __init__(self, title, writer, year, publisher, pages, stat="대출가능"):
        self.title = title  # 서명
        self.writer = writer  # 작가
        self.year = year  # 출판년도
        self.publisher = publisher  # 출판사
        self.pages = pages  # 쪽수

        self.book_stat = stat  # 책 상태 (대출중, 예약중, 대출 가능 등등..)
        self.borrow_user = ""  # 대출중이라면 대출한 이용자
        self.booking_user = []  # 예약중이라면 예약한 이용자

    # 책 정보 출력
    def print_book(self):
        print("서명: " + self.title)
        print("작가: " + self.writer)
        print("출판년도: " + str(self.year))
        print("출판사: " + self.publisher)
        print("쪽수: " + str(self.pages))

    # 책 상태 조회
    def show_book_stat(self):
        print("현재", self.borrow_stat, "상태인 도서입니다.")

    # 책 대출 및 예약
    def booking(self, user):
        # 책 대출
        if self.borrow_state == "대출가능":
            print("현재 대출 가능한 도서입니다.")
            if "Y" == input("대출하시겠습니까?: Y/N"):
                self.borrow_user = user
                self.borrow_stat == "대출중"

        # 책 예약
        elif self.borrow_state == "대출중":
            print("현재 대출중인 도서입니다")
            if "Y" == input("예약하시겠습니까?: Y/N"):
                self.booking_user.append(user)
                self.borrow_stat == "예약중"

        else:  # 대출중이며 예약도 된 상태
            print("현재 예약중인 도서입니다")
