class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def stockdata(self):
        return f'주식명:{self.name} 주식코드:{self.code}'

    @staticmethod
    def del_element(ls, code):
        for i, j in enumerate(ls):
            if j.name == code:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.EXIT\n 1.입력\n 2.출력\n 3.수정\n 4.삭제')
            if menu == '0':
                break

            elif menu == '1':
                stock = Stock(input("주식명:"), input("주식코드:"))
                ls.append(stock)

            elif menu == '2':
                for i in ls:
                    print(f'주식종목 리스트:{i.stockdata()}')

            elif menu == '3':
                code = input('종목코드: ')
                stock = Stock(input('수정할 이름'), code)
                stock.del_element(ls, code)
                ls.append(stock)

            elif menu == '4':
                stock = Stock(None, input('종목코드'))
                stock.del_element(ls, stock)

            else:
                print('잘못된 주문입니다.')
                continue

Stock.main()