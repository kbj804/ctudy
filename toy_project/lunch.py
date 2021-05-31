import random
lunch_list = ['오돈', '배꼽집', '대문집', '진주집', '채', '김']
d= random.choice(lunch_list)
print(d)


def select_lunch(lunch:list):
    for i in range(0, len(lunch)):
        random.shuffle(lunch)
    return lunch[0]

print(select_lunch(lunch_list))