import random

class Account(object):
    def __init__(self, name, account_nbr, money):
        self.BANK_NAME = "sc은행"
        self.name = name
        self.account_nbr = account_nbr
        self.money = money
    '''
    계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
    '''

    def get_account(self):
        return f'은행명:{self.BANK_NAME} 예금주:{self.name} 계좌번호:{self.account_nbr} 잔액:{self.money}'

    @staticmethod
    def create_account_number():
        ls = [str(random.randint(0,9)) for i in range(3)]
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(2):
            ls.append(str(random.randint(0,9)))
        ls.append('-')
        for i in range(6):
            ls.append(str(random.randint(0, 9)))
        return "".join(ls)

    @staticmethod
    def del_account(ls, account_nbr):
        for i, j in enumerate(ls):
            if j.account_nbr == account_nbr:
                del ls[i]

    @staticmethod
    def add_sub(ls, account_nbr, money):
        for i, j in enumerate(ls):
            if j.account_nbr == account_nbr:
                replace = Account(j.name
                                  ,j.account_nbr
                                  ,int(j.money) + int(money)
                                  , int(j.money) - int(money)) # 출금 -
                Account.del_account(ls, account_nbr)
                ls.append(replace)

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌탈퇴')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Account(input('name'),
                                  Account.create_account_number(),
                                  input('money')))

            elif menu == '2':
                for i in ls:
                    print(i.get_account())

            elif menu == '3':
                account_nbr = input('입금할 계좌번호')
                money = input ('입금액 입력바랍니다')
                for i, j in enumerate(ls):
                    if j.account_nbr == account_nbr:
                        replace = Account(j.name,
                                          j.account_nbr,
                                          int(j.money)+int(money)) #입금 +
                        Account.del_account(ls, account_nbr)
                        ls.append(replace)

            elif menu == '4':
                account_nbr = input('출금할 계좌번호')
                money = input('출금액 입력바랍니다')
                Account.add_sub(ls, input)

            elif menu == '5':
                Account.del_account(ls, input('삭제할 계좌번호'))

            else:
                print('Wrong Number')
            continue

Account.main()

