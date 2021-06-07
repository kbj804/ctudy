import random
stop_word = ['오돈']
lunch_list = ['배꼽집', '대문집', '진주집', '채', '김', '중국집', '쌀국수', '고등어', '분식', '순대국']
d = random.choice(lunch_list)



def select_lunch(lunch:list):
    for i in range(0, len(lunch)):
        random.shuffle(lunch)
    return lunch[0]

print(select_lunch(lunch_list))