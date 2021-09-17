# hasattr 함수
# 객체가 있는경우와 없는경우에 따라 분기가 달라지게 할 수 있음
class Car:
    def __init__(self) -> None:
        self.build_frame()
        self.build_engine()
        # self.build_wheel()

    def build_frame(self):
        self.frame = 'frame 조립 완료'
        print("frame ... structure ... Complete")
    
    def build_engine(self):
        self.engine = 'engine 조립 완료'
        print("engine ... structure ... Complete ")

    def build_wheel(self):
        self.wheel = 'whell 조립 완료'
        print("wheel ... structure ... Complete")
    
    def check(self):
        checklist = ['frame', 'engine', 'wheel']
        for part in checklist:
            if hasattr(self, part):
                print(f"{part} ... check ... OK")
            else:
                print(f"WARNING!! 자동차에 {part}이 없습니다.")

genesis = Car()
genesis.check()

