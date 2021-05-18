def bmi_function(height, weight):
    return weight / height ** 2 * 10000


class Bmi(object):

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def getBmi(self):
        return self.weight / self.height ** 2 * 10000


if __name__ == '__main__':
    pass
    #b = Bmi(180, 70)
    #print(b.getBmi())
    print(bmi_function(180,70))


    """
    최소한의 코드로 최고의 퍼포먼스를 뽑아내는 것"""