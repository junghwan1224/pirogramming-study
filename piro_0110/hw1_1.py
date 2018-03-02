import sys

price = [1000,700,1200]
count = [5,5,5]
bev ={
    1 : '사이다',
    2 : '콜라',
    3 : '비타500'
}

def print_menu():
    print('No.\tName\tPrice')
    print('1.\t사이다\t1000')
    print('2.\t콜라\t700')
    print('3.\t비타500\t1200')

def insert_money():
    money = int(input('insert money(800 ~ 5000) : '))
    while True:
        if money < 800 or money > 5000:
            print('insert 800 ~ 5000')
            money = int(input('insert money(800 ~ 5000) :'))
        else:
            return money
            break

def enter_num_and_calc_money(money):
    num = int(input('enter number : '))
    print('You choice ' + bev[num])
    left_money = money - price[num-1]
    count[num-1] -= 1
    print('Left money :',left_money)
    while True:
        num = int(input('enter number : '))

        if count[num-1] <= 0:
            print('This product is sold out.')
            print('Please choose other one.')
        else:
            if left_money < price[num-1]:
                print('You do not have enough money to buy this beverage')
                sys.exit(1)
            else:
                left_money -= price[num-1]
                count[num-1] -= 1
                print('Left money :',left_money)

print_menu()
money = insert_money()
enter_num_and_calc_money(money)