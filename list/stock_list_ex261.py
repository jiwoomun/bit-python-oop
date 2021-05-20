class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def stockdata(self):
        return f'주식명:{self.name} 주식코드:{self.code}'
    pass

    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.EXIT\n 1.입력\n 2.출력')
            if menu == '0':
                break
            elif menu == '1':
                ls.append(Stock(input("주식명:"), input("주식코드:")))
            elif menu == '2':
                for i in ls:
                    print(f'주식종목 리스트:{i.stockdata()}')
            else:
                print('잘못된 주문입니다.')
                continue

Stock.main()