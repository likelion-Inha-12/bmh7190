from 실습2 import bank

class bank2(bank):
    # 생성자
    def __init__(self, name, money, plus):
        super().__init__(name, money)
        self.plus = plus

    # 입금할 때 현재 잔액 / 이자율 표시
    def input_money(self, in_money):

        print("%s님의 계좌 잔액은 %d원입니다." %(self.name, self.money))
        print("이자율: %.1f%%" %self.plus)

        self.money = self.money + in_money

        print("%d이 입금되었습니다." %in_money)

    # 추가이자율
    def plusplus(self):

        plusmoney = self.money*(self.plus/100)
        self.money = self.money + plusmoney

        print("%s님의 계좌에 %.1f원의 이자가 추가되었습니다." %(self.name, plusmoney))

    # 현재 잔액 + 이자율 확인
    def check_money(self):

        print("%s님의 계좌 잔액은 %.1f원입니다." %(self.name,self.money))
        print("이자율: %.1f%%" %self.plus)

# 예시 입력
""" customer = bank2("dongha", 1000, 5)
customer.input_money(500)
customer.plusplus()
customer.output_money(100)
customer.check_money() """