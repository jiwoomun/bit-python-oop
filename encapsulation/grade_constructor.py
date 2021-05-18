class Grade:
    def setGrade(self,ko,en,mth,so):
        self.ko=ko
        self.en=en
        self.mth=mth
        self.so=so

    def sum(self):
        return g.ko+g.en+g.mth+g.so

    def avg(self):
        return self.sum() /4

if __name__ == '__main__':
    g= Grade()
    g.setGrade(100,80,60,40)
    print(g.sum())
    print(g.avg())