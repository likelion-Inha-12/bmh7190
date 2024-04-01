class bank:
    # 생성자
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # 입금하기
    def input_money(self,in_money):
        self.money = self.money + in_money

        print("%d원이 입금되었습니다." %in_money)

    # 출금하기
    def output_money(self,out_money):
        if(self.money<out_money or out_money<=0):
            print("출금 금액이 잔액을 초과하거나 잘못 입력되었습니다.")
        
        else:
            self.money = self.money - out_money
            print("%d원이 출금되었습니다" %out_money)
        
    # 잔액확인하기
    def check_money(self):
        print("%s님의 계좌 잔액은 %d원입니다." %(self.name,self.money))

# 예시 입력
""" customer = bank("dongha",1000)
customer.check_money()
customer.input_money(500)
customer.output_money(200)
customer.check_money() """