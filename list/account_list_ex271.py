class Account(object):
    def __init__(self, name, balance, account_nbr):
        self.name = name
        self.balance = balance
        self.BANK_NAME = "sc은행"
        self.account_nbr = account_nbr

    def get_account(self):
        return f'은행명:{self.bank} 예금주:{self.name} 계좌번호:{self.nbr} 잔액:{self.sum}'

    @staticmethod
    def main():
        while 1:
            menu = input('0.EXIT\n1.입력\n2.출력')
            if menu == '0':
                break
            elif menu == '1':
                account=Account(input("예금주:"),random.randrange("계좌번호:")(0-999),input("잔액:"))

            elif menu == '2':
                print(account.get_account())

            else:
                print('잘못된 주문입니다.')
            continue

Account.main()


