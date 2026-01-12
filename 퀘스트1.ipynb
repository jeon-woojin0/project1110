import random as r

class Account :#계좌 입출금 클래스
    account_count = 0 #계좌수 세는 
    def __init__(self,name,balance): #생성자
        self.bank = 'SC 제일은행'
        self.name = name 
        num = "" #빈 숫자 생성 
        for i in range(9) : 
            num += str(r.randint(0,9)) #string에 추가 9번
            if i == 2 or i == 4: 
                num += "-" # index 2, 4 다음에 하이푼 추가
        self.num = num #위의 for문의 난수를 받는 계좌번호 (111-11-1111)
        self.balance = balance #초기잔액
        Account.account_count += 1 #계좌 개수
        self.deposit_count = 0 #입금횟수
        self.withdraw_count = 0 #출금횟수
        self.history1 = [] #입금 history 기록용 리스트
        self.history2 = [] # 출금 history 기록용 빈 리스트
        
    
    def __str__(self): #매직 method
        return(f"은행:{self.bank}, 계좌번호:{self.num}, 잔액:{self.balance:,}원.")
    
    def get_account_num(self) : #생성된 계좌 개수 출력
        print(f"총 계좌 개수:{Account.account_count}개") 

    def deposit(self,money): #입금method
        if money < 1 :
            print("최소 1원 이상 입금가능")
        
        self.deposit_money = money
        self.balance += money
        self.deposit_count += 1
        self.history1.append(f"{self.deposit_money}원 입금")

        if self.deposit_count % 5==0: #입금횟수 5의배수가 되면 이자 지급
            interest = self.balance * 0.01 
            self.balance += interest
            print(f"{self.deposit_money}원 입금 \n{self.deposit_count}회입금, 이자{interest}원 지급, 잔액: {self.balance:,}원") 

        else :
            print(f"{self.deposit_money}원 입금, 잔액:{self.balance}원")

    def withdraw(self,withdraw_money): #출금method
        self.money = withdraw_money
        
        if self.money > self.balance: #출금 조건
            print(f"잔액 {self.balance}원보다 큰 금액은 출금 불가")
        else :
            self.withdraw_count += 1
            self.history2.append(f"{withdraw_money}원 출금")
            self.balance -= withdraw_money
            print(f"{withdraw_money}원 출금 \n현재 잔액:{self.balance:,}원")

    def deposit_history(self):
        self.history1.insert(0,f"총{self.deposit_count}회 입금")
        return(print(self.history1))
  
    def withdraw_history(self):
        self.history2.insert(0,f"총{self.withdraw_count}회 출금")
        return(print(self.history2))

    def display_info(self) : #인스턴스 정보 출력
        return(f"은행이름:{self.bank}, 예금주:{self.name}, 계좌번호:{self.num}, 잔고:{self.balance:,}원")

#인스턴스 3개 이상만들기
ac1 = Account('전우진',1000000)
ac2 = Account('한지수',40000)
ac3 = Account('윤서연',60000)

#입금 구현 + 이자
ac1.deposit(100000)
ac1.deposit(100000)
ac1.deposit(100000)
ac1.deposit(100000)
ac1.deposit(100000)
ac1.display_info()

#입금 히스토리 구현
ac1.deposit_history()

#총 계좌 개수, 클래스 변수(?) 로 Account.account_count로 세기
ac1.get_account_num()

#출금 구현, 잔고 이상출금 불가
ac2.withdraw(50000)
ac2.withdraw(10000)
ac2.display_info()

ac2.withdraw_history()
ac3.deposit(1000000)

account = [ac1, ac2 ,ac3] #100만원 이상 고객 찾기
for ac in account:
    if ac.balance >= 1000000:
        print(f"100만원 이상 고객: {ac.name}")
