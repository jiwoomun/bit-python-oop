'''
이름, 전화번호, 이메일, 주소를 받아서 연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
'''


class Contacts(object):
    def __init__(self,name,nbr,email,adr):
        self.name = name
        self.nbr = nbr
        self.email = email
        self.adr = adr

    def get_contact(self):
        return f'주소록: 이름{self.name}, 전화번호{self.nbr}, 이메일{self.email}, 주소{self.adr}'

    @staticmethod
    def main():
        ls =[]
        while 1:
            menu = input('0.EXIT 1.입력 2.출력')
            if menu == '0':
                break

            elif menu == '1':
                ls.append(Contacts(input('이름:'), input('전화번호'), input('이메일'), input('주소')))

            elif menu == '2':
                for i in ls:
                    print(f'출력결과:{i.get_contact()}')

            else:
                print('잘못된 주문입니다.')
                continue


Contacts.main()