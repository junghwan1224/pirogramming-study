import random
import sys

name = input()
ans = int(input())
rand_num = random.randint(1,20)
count = 1

while True:
    if ans > rand_num :
        print('Your answer is more than computer number')
        count += 1
        ans = int(input())
    elif ans < rand_num :
        print('Your answer is less than computer number')
        count += 1
        ans = int(input())
    else:
        print('Good Job!!',name,'!!')
        print('Count :',count)
        ans = int(input())
        sys.exit(1)