import random
import sys

#가위 1, 바위 2, 보 3
user =input()
npc = random.randint(1,3)
win = 0
lose = 0
draw = 0

if user == 'q' or user == 'Q':
    print('program end')
    sys.exit(1)
#else:
    #user = int(user)

while True:

    if user == '1':#가위
        if npc == 1:
            print('draw','user : 가위 / npc : 가위')
            draw += 1
            npc = random.randint(1,3)
            user = input()
        elif npc == 2:
            print('lose','user : 가위 / npc : 바위')
            lose += 1
            npc = random.randint(1,3)
            user = input()
        else:
            print('win','user : 가위 / npc : 보')
            win += 1
            npc = random.randint(1,3)
            user = input()

    elif user == '2':#바위
        if npc == 1:
            print('win','user : 바위 / npc : 가위')
            win += 1
            npc = random.randint(1,3)
            user = input()
        elif npc == 2:
            print('draw','user : 바위 / npc : 바위')
            draw += 1
            npc = random.randint(1,3)
            user = input()
        else:
            print('lose','user : 바위 / npc : 보')
            lose += 1
            npc = random.randint(1,3)
            user = input()

    elif user == '3':#보
        if npc == 1:
            print('lose','user : 보 / npc : 가위')
            lose += 1
            npc = random.randint(1,3)
            user = input()
        elif npc == 2:
            print('win','user : 보 / npc : 바위')
            win += 1
            npc = random.randint(1,3)
            user = input()
        else:
            print('draw','user : 보 / npc : 보')
            draw += 1
            npc = random.randint(1,3)
            user = input()

    elif user == 'q' or user == 'Q':
        print('Your grade : win =',win,'draw =',draw,'lose =',lose)
        print('program end')
        sys.exit(1)

    else:
        print('retry')
        user = input()