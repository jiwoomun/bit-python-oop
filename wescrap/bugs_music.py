class BugsMusic(object):

    def __init__(self,url):
        self.url = url

    def to_string(self) -> str:
        return self.url

    @staticmethod
    def main():
        while 1:
            menu= int(input('0.Exit\n 1.Input URL \n 2.Print URL'))
            if menu == 0:
                break
            elif menu == 1:
                bugs = BugsMusic(input('Input URL'))
            elif menu == 2:
                print(f'Input URL is {bugs.to_string()}')
            else:
                print('Wrong Number')
                continue


BugsMusic.main()