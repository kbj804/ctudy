import sys

class RefExam():
  def __init__(self):
    print('create object')

a = RefExam()
print(f'count {sys.getrefcount(a)}')
b = a
print(f'count {sys.getrefcount(a)}')
c = a
print(f'count {sys.getrefcount(a)}')
c = 0
print(f'count {sys.getrefcount(a)}')
b = 0
print(f'count {sys.getrefcount(a)}')

"""
OUT PUT:
count 2
count 3
count 4
count 3
count 2
"""


class RefExam():
    def __init__(self):
        print('create object')
    def __del__(self):
        print(f'destroy {id(self)}')


a = RefExam()
a = 0
print('end .....')

"""
OUT PUT:
create object
destroy 3112733520336
end .....
"""


# me 프로퍼티에 자기 자신을 할당합니다.
class RefExam():
  def __init__(self):
    print('create object')
    self.me = self
  def __del__(self):
    print(f'destroy {id(self)}')

a = RefExam()
a = 0
print('end .....')

"""
OUT PUT:
create object
end .....
destroy 2110595412432
"""


import gc
print(gc.get_threshold())
print(gc.get_count())
"""
OUTPUT:
(700, 10, 10)
(18, 7, 8)              // 현재 count상태를 확인하는 것이기 때문에 출력값이 다를 수 있다.
"""



