class Grade(object):
    def __init__(self, kor, eng, mth):
        self.kor = kor
        self.eng = eng
        self.mth = mth

    def sum(self):
        return self.kor + self.eng + self.mth
    def avg(self):
        return self.sum()/3

    def get_grade(self):
        score = int(self.avg())
        grade = ''
        if score >= 90:
            grade = 'A학점'
        elif score >= 80:
            grade = 'b학점'
        elif score >= 70:
            grade = 'c학점'
        elif score >= 60:
            grade = 'd학점'
        elif score >= 50:
            grade = 'e학점'
        else:
            grade = 'f학점'



        return grade

    @staticmethod
    def main():
        g = Grade(int(input('국어')), int(input('영어')), int(input('수학')))
        print(f'총점: {g.sum()}')
        print(f'평균: {g.avg()}')
        print(f'학점: {g.get_grade()}')

Grade.main()
