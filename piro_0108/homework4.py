import random

alchol_or_meal = input() #뒤풀이 또는 식사 입력
meal_place = ['화양리','서울대입구','건대']
meal_food = ['일식','양식','중식']
alchol_place = ['지그재그','홍콩포차','일광']
alchol = ['소주','맥주','소맥']

if alchol_or_meal == '뒤풀이':
    alchol_result = ''
    while True:
        alchol_str = input('뒤풀이 장소와 종류 입력 : ')
        if alchol_str == 'end' or alchol_str == 'End':
            break
        alchol_result += alchol_str
    random_q = input('랜덤뽑기?')
    if random_q == 'yes':
        alchol_place_random = random.choice(alchol_place)
        alchol_random = random.choice(alchol)
        print('뒤풀이 랜덤뽑기 결과 :',alchol_place_random,alchol_random)
    else:
        print('뒤풀이 입력 결과 : ',alchol_result)

elif alchol_or_meal == '식사':
    meal_result = ''
    while True:
        meal_str = input('식사 장소와 종류 입력 : ')
        if meal_str == 'end' or meal_str == 'End':
            break
        meal_result += meal_str

    alchol_result = ''
    while True:
        alchol_str = input('뒤풀이 장소와 종류 입력 : ')
        if alchol_str == 'end' or alchol_str == 'End':
            break
        alchol_result += alchol_str

    random_q = input('랜덤뽑기?')
    if random_q == 'yes':
        alchol_place_random = random.choice(alchol_place)
        alchol_random = random.choice(alchol)
        print('뒤풀이 랜덤뽑기 결과 :',alchol_place_random,alchol_random)
    else:
        print('뒤풀이 입력 결과 : ',alchol_result)