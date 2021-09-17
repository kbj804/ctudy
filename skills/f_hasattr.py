# hasattr 함수
# 객체가 있는경우와 없는경우에 따라 분기가 달라지게 할 수 있음
class A:
    def method(self):
        self.a = '하이'
    def test(self):
        if hasattr(self, 'a'):
            print(self.a)
        else:
            print("출력 20")

temp = A()
temp.test()

temp.method()
temp.test()