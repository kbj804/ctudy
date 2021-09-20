# 싱글톤 디자인 패턴
# Logging, DB 같은 동일한 리소스에 대한 동시 요청 충돌 방지
# 방법: Constructor를 private로 선언 후 객체 초기화 함수(static) 생성

class Singleton(object):
    def __new__(cls):
        # 객체가 있는지 확인
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)


# Lazy instantiation - 꼭 필요한 인스턴스일 경우 생성(리소스 제한적일때 또한 필요한 시점에 생성 가능)

class Singleton_Layz:
    __instance = None
    def __init__(self) -> None:
        if not Singleton.__instance:
            print("__init__ method called ... ")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()

        return cls.__instance

s2 = Singleton_Layz() # 클래스는 초기화 했지만 객체 생성 X
print("Object created", Singleton_Layz.getInstance()) # 여기서 객체 생성
s3 = Singleton_Layz() # 객체 생성된거 포함