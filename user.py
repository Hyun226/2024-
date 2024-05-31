class User:
# 이용자 등록
# __init__는 클래스를 생성할 때, 실행되는 함수
    def __init__(self, name, year, address, sex, job):
        self.name = name   # 이름
        self.year = year   # 출생년도
        self.address = address   # 주소
        self.sex = sex   # 성별
        self.job = job   # 직업

# 이용자 정보 출력
    def print_user(self):
        print("이름: " + self.name)
        print("출생년도: " + str(self.year))
        print("주소: " + self.address)
        print("성별: " + self.sex)
        print("직업: " + self.job)
