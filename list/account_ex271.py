import random

class Account(object):
    def __init__(self, name, account_nbr, money):
        self.BANK_NAME = "sc은행"
        self.name = name
        self.account_nbr = self.create_account_number(3)
        self.money = money
    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''

    def create_account_number(self):
        ls = []
        for i in range(3):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    def get_account(self):
        return f'은행명:{self.BANK_NAME} 예금주:{self.name} 계좌번호:{self.account_nbr} 잔액:{self.money}'

    @staticmethod
    def main():
        while 1:
            menu = input('0.EXIT 1.Create 2.Read 3.Update 4,Delete')
            if menu == '0':
                break
            elif menu == '1':
                account = Account(input('name'),
                                  input('name'))

            elif menu == '2':
                print(account.get_account())

            elif menu == '3':
                pass

            elif menu == '4':
                pass


            else:
                print('잘못된 주문입니다.')
            continue

Account.main()


