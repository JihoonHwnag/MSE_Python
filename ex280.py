# 숫자를 무작위로 뽑기 위해 random 모듈 불러오기
import random


class Account:
    # class variable (클래스 공간 안에 변수 생성)
    account_count = 0
	
	# 생성자 __init__ 생성, 
    def __init__(self, name, balance):
		# 예금횟수 초기값을 0으로 설정
        self.deposit_count = 0
		# 예금 내역과 출금 내역을 리스트로 구성
        self.deposit_log = []
        self.withdraw_log = []
		
		# name의 자리에 이름, balance의 자리에 잔고 저장
        self.name = name
        self.balance = balance
		# 은행이름 설정 
        self.bank = "SC은행"

        # 계좌번호 3-2-6 만들기 
		# random 모듈 속 randint 함수를 사용하여 구간 속 숫자를 랜덤으로 뽑아옴
        num1 = random.randint(0, 999) # 0 <= i <= 999
        num2 = random.randint(0, 99) # 0 <= i <= 99
        num3 = random.randint(0, 999999) # 0 <= i <= 999999

		# 무작위로 뽑은 수를 문자열 str로 변경, 자릿수를 맞추기 위해 zfill() 메서드 사용 
        num1 = str(num1).zfill(3)  # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)  # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)  # 1 -> '1' -> '0000001'
		# 계좌번호 형식 만들기    001-01-000001
        self.account_number = num1 + '-' + num2 + '-' + num3  
		
		# 계좌의 개수를 뜻하며, 계좌가 만들어질 때마다 증가
        Account.account_count += 1

    @classmethod 
	# account_count는 클래스 공간에 저장되어 있기 때문에 메서드를 호출하는 객체 공간을 구별하기 위한 변수인 self를 받을 필요 없음
    def get_account_num(cls):
        print(cls.account_count)  # Account.account_count

	# 잔고는 특정 객체 안에 존재하므로 객체에 접근하기 위해 self 사용, 입금액을 amount로 바인딩
    def deposit(self, amount):
		# 1원 이상일 때 입금 가능 식 구현
        if amount >= 1:
			# 입금액을 deposit_log에 추가
            self.deposit_log.append(amount)
            self.balance += amount

            self.deposit_count += 1
			# 예금 내역이 증가했을 때 5의 배수를 확인하는 식 작성
            if self.deposit_count % 5 == 0:         # 5, 10, 15
                # 이자 지급
                self.balance = (self.balance * 1.01)

	# 이 또한 잔고는 특정 객체 안에 존재하므로 self 사용, 출금 요청액을 amount로 바인딩
    def withdraw(self, amount):
		# 잔고가 출금 요청액보다 많은지 확인
        if self.balance > amount:
			# 출금액을 withdraw_log에 추가
            self.withdraw_log.append(amount)
            self.balance -= amount

	# Account 인스턴스에 저장된 정보를 출력하는 display_info 메서드 정의
    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ", self.balance)

	# 출금 금액을 출금 내역에서 가져와 출력하는 메서드 작성
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

	# 입금 금액을 입금 내역에서 가져와 출력하는 메서드 작성
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

# 클래스 Account 안의 변수들에 접근, 객체 적용 
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
