class Stock(object):
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def stockdata(self):
        return f'주식명:{self.name} 주식코드:{self.code}'


    @staticmethod
    def main():
        ls = []
        while 1:
            menu = input('0.EXIT\n 1.입력\n 2.출력\n 3.수정\n 4.삭제')
            if menu == '0':
                break

            elif menu == '1':
                ls.append(Stock(input("주식명:"), input("주식코드:")))

            elif menu == '2':
                for i in ls:
                    print(f'주식종목 리스트:{i.stockdata()}')

            elif menu == '3':
                edit_name = input('수정할 종목명: ')
                edit_info = Stock(edit_name, input('수정 코드'))
                for i, j in enumerate(ls):
                    if j.name == edit_name:
                        del ls[i]
                        ls.append(edit_info)

            elif menu == '4':
                del_name = input('삭제할 종목: ')
                for i, j in enumerate(ls):
                    if j.name == del_name:
                        del ls[i]

            else:
                print('잘못된 주문입니다.')
                continue

Stock.main()